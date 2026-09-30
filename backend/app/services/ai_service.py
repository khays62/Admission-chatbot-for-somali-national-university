import json
import logging
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR / ".env.local")


class OpenRouterAIService:
    def __init__(self):
        self.api_key = os.environ.get("OPENROUTER_API_KEY", "")
        self.model = os.environ.get("OPENROUTER_MODEL", "openai/gpt-oss-20b:free")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

    def is_configured(self):
        return bool(self.api_key)

    def _parse_rate_limit(self, response):
        try:
            body = response.json()
        except Exception:
            body = {}

        error = body.get("error", {})
        metadata = error.get("metadata", {}) or {}
        retry_seconds = metadata.get("retry_after_seconds") or metadata.get("retry_after_seconds_raw")
        if retry_seconds is None:
            retry_seconds = response.headers.get("Retry-After")
        return {
            "status_code": response.status_code,
            "provider": metadata.get("provider_name"),
            "retry_after_seconds": int(retry_seconds) if str(retry_seconds).isdigit() else None,
            "message": error.get("message") or response.text,
        }

    def generate(self, prompt, system_prompt=None):
        if not self.is_configured():
            return {"ok": False, "error": "missing_api_key", "content": None}

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://localhost:5000",
            "X-Title": "SNU Admission Assistant",
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.4,
        }

        for attempt in range(2):
            try:
                response = requests.post(self.base_url, headers=headers, json=payload, timeout=30)
                print("DEBUG_OPENROUTER_STATUS", response.status_code)
                print("DEBUG_OPENROUTER_BODY", response.text[:1500])

                if response.status_code == 429:
                    rate_limit = self._parse_rate_limit(response)
                    print("DEBUG_OPENROUTER_RATE_LIMIT", json.dumps(rate_limit, ensure_ascii=False))
                    if attempt == 0:
                        retry_after = rate_limit.get("retry_after_seconds") or 5
                        time.sleep(min(retry_after, 6))
                        continue
                    return {"ok": False, "error": "rate_limited", "content": None, "meta": rate_limit}

                response.raise_for_status()
                data = response.json()
                choices = data.get("choices", [])
                if not choices:
                    logger.warning("OpenRouter returned no choices: %s", data)
                    print("DEBUG_OPENROUTER_NO_CHOICES", data)
                    return {"ok": False, "error": "no_choices", "content": None}

                content = choices[0].get("message", {}).get("content", "")
                cleaned = content.strip() if isinstance(content, str) else None
                return {"ok": True, "error": None, "content": cleaned}
            except requests.exceptions.HTTPError as exc:
                logger.exception("OpenRouter request failed for model %s: %s", self.model, exc)
                print("DEBUG_OPENROUTER_EXCEPTION", type(exc).__name__, str(exc))
                return {"ok": False, "error": "http_error", "content": None}
            except Exception as exc:
                logger.exception("OpenRouter request failed for model %s: %s", self.model, exc)
                print("DEBUG_OPENROUTER_EXCEPTION", type(exc).__name__, str(exc))
                return {"ok": False, "error": "request_failed", "content": None}

        return {"ok": False, "error": "request_failed", "content": None}


def build_ai_response(prompt, system_prompt=None):
    service = OpenRouterAIService()
    result = service.generate(prompt, system_prompt=system_prompt)
    return result.get("content") if result.get("ok") else None
