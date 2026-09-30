from flask import Blueprint, jsonify, request, session

from app.config import DEFAULT_PROVIDER, OPENROUTER_API_KEY
from app.services.ai_service import build_ai_response
from app.services.intent_service import build_chatbot_response
from app.services.session_service import clear_session, ensure_session, get_session_state, initialize_session

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/api")


def create_ai_system_prompt():
    return (
        "Waxaad tahay caawiye admission-ka ee SNU. "
        "Jawaabaha ku bixid af-Soomaali ah, gaaban, cad, oo la fahmi karo. "
        "Ha sheegin macluumaad aan la hubin. "
        "Haddii su'aal tahay shuruudaha codsiga, dokumentiyada, lacag bixinta, ama link-ga rasmiga ah, "
        "u sheeg jawaab sax ah oo ku salaysan xogta SNU. "
        "Haddii aad haysato link rasmi ah, sii link-ka. "
        "Haddii su'aasha aanay cadayn, weydii hal su'aal oo la fahmi karo. "
        "La hadal user-ka si niyad ahaan, si toos ah, oo dhammaystir jawaabtaaga dhawr xabbood oo kaliya."
    )


@chatbot_bp.route("/chat/message", methods=["POST"])
def chat_message():
    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()

    if not message:
        return jsonify({"success": False, "error": "Message required"}), 400

    ensure_session()
    result = build_chatbot_response(message)
    provider_status = {
        "provider": "rule_based",
        "available": True,
        "rate_limited": False,
        "fallback_used": False,
    }

    if result["intent"] in ["greeting", "redirect", "faq", "contact"]:
        final_response = result["chatbot_response"]
        final_intent = result["intent"]
        final_type = result["response_type"]
    else:
        if DEFAULT_PROVIDER == "openrouter" and OPENROUTER_API_KEY:
            ai_response = build_ai_response(message, system_prompt=create_ai_system_prompt())
            if ai_response:
                final_response = ai_response
                final_intent = "ai_fallback"
                final_type = "ai"
                provider_status = {"provider": "openrouter", "available": True, "rate_limited": False, "fallback_used": False}
            else:
                final_response = result["chatbot_response"]
                final_intent = result["intent"]
                final_type = result["response_type"]
                provider_status = {"provider": "openrouter", "available": False, "rate_limited": True, "fallback_used": True}
        else:
            final_response = result["chatbot_response"]
            final_intent = result["intent"]
            final_type = result["response_type"]

    response_payload = {
        "success": True,
        "chatbot_response": final_response,
        "intent": final_intent,
        "response_type": final_type,
        "session_token": session.get("session_token"),
        "message_count": session.get("message_count", 0),
        "next_actions": result["next_actions"],
        "provider_status": provider_status,
    }

    return jsonify(response_payload)


@chatbot_bp.route("/chat/session/start", methods=["POST"])
def start_session():
    token = initialize_session()
    return jsonify({
        "success": True,
        "session_token": token,
        "message_count": 0,
        "message": "Session created",
    })


@chatbot_bp.route("/chat/session/reset", methods=["POST"])
def reset_session():
    clear_session()
    return jsonify({
        "success": True,
        "message": "Session cleared",
    })


@chatbot_bp.route("/chat/session/state", methods=["GET"])
def session_state():
    state = get_session_state()
    return jsonify({
        "success": True,
        "session_token": state["session_token"],
        "is_active": state["is_active"],
        "message_count": state["message_count"],
    })


@chatbot_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
