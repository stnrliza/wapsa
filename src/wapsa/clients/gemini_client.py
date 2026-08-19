from __future__ import annotations

import requests
from typing import Optional
from wapsa.config.settings import settings

class GeminiClient:
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or settings.gemini_api_key
        self.model = model or settings.gemini_model

    def classify(self, message: str, categories: list[str]) -> str:
        url = f"{self.BASE_URL}/{self.model}:generateContent"
        prompt = (
            f"Klasifikasikan pesan ini ke salah satu kategori: {', '.join(categories)}. "
            f"Pesan: '{message}'. Jawab HANYA dengan satu kata kategori tersebut."
        )
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(
            url,
            headers={"Content-Type": "application/json", "x-goog-api-key": self.api_key},
            json=payload,
        )
        response.raise_for_status()
        try:
            text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as e:
            raise RuntimeError(f"Unexpected Gemini response: {response.text}") from e
        return text.strip().strip(".,!").title()
