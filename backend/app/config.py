import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR / ".env.local")

SECRET_KEY = os.environ.get("SECRET_KEY", "snu-chatbot-secret-key")
SESSION_COOKIE_NAME = "snu_chatbot_session"
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
SESSION_REFRESH_EACH_REQUEST = True

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "openai/gpt-oss-20b:free")
DEFAULT_PROVIDER = os.environ.get("DEFAULT_PROVIDER", "openrouter")
APP_ENV = os.environ.get("APP_ENV", "development")
