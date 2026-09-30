import re

from app.services.knowledge_service import get_contact_info, get_faq_items


def normalize_text(text):
    text = (text or "").strip().lower()
    return re.sub(r"[^a-z0-9\s]", " ", text)


def detect_intent(message):
    text = normalize_text(message)
    if not text:
        return "unknown"

    greeting_keywords = ["hello", "hi", "salaam", "soo dhawoow", "salaan"]
    redirect_keywords = ["isdiiwaan gelin", "diiwaan gelin", "apply", "codsi", "register", "iska diiwaan gelin"]
    faq_keywords = ["shuruud", "requirements", "dokument", "document", "lacag", "pay", "bank", "kuliyad", "faculty", "xarun", "campus", "imtixaan", "exam"]
    contact_keywords = ["contact", "xiriir", "help", "support", "noqo"]

    if any(keyword in text for keyword in greeting_keywords):
        return "greeting"
    if any(keyword in text for keyword in redirect_keywords):
        return "redirect"
    if any(keyword in text for keyword in faq_keywords):
        return "faq"
    if any(keyword in text for keyword in contact_keywords):
        return "contact"
    return "out_of_scope"


def answer_faq(message):
    text = normalize_text(message)
    for item in get_faq_items():
        question = normalize_text(item.get("q", ""))
        if question in text or text in question:
            return item.get("a", "")
    return "Waxaan ku caawin karaa shuruudaha, dokumentiyada, lacag bixinta, ama link-ga codsiga. Ma rabtaa inaad ka bacaato mid ka mid?"


def build_chatbot_response(message):
    intent = detect_intent(message)

    if intent == "greeting":
        response = "Ku soo dhawoow! Waxaan kaa caawin karaa shuruudaha, dokumentiyada, lacag bixinta, ama link-ga codsiga."
        response_type = "greeting"
    elif intent == "redirect":
        response = "Waxaad ka bilaabi kartaa bogga codsiga rasmiga ah: https://student.snu.edu.so/admission/online-application"
        response_type = "redirect"
    elif intent == "faq":
        response = answer_faq(message)
        response_type = "faq"
    elif intent == "contact":
        contact = get_contact_info()
        phone = ", ".join(contact.get("phone", ["N/A"]))
        email = contact.get("email", "N/A")
        response = f"Xiriir: {phone}. Email: {email}."
        response_type = "contact"
    else:
        response = "Waxaan ku takhasusay su'aalaha admission-ka. Ma rabtaa inaan kaa caawiyo shuruudaha gelitaanka, dokumentiyada, ama link-ga codsiga?"
        response_type = "out_of_scope"

    return {
        "intent": intent,
        "response_type": response_type,
        "chatbot_response": response,
        "next_actions": ["Codsiga", "Shuruudaha", "Dokumentiyada", "Lacag bixinta"],
    }
