import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_PATH = BASE_DIR / "data" / "knowledge_base.json"


def get_knowledge():
    with KNOWLEDGE_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_faq_items():
    return get_knowledge().get("faq", [])


def get_contact_info():
    return get_knowledge().get("contact_info", {})


def get_admission_links():
    return get_knowledge().get("admission_links", {})
