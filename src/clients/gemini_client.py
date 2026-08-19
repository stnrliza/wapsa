import json
import requests
from config.settings import settings

class GeminiClient:
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"

    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key or settings.gemini_api_key
        self.model = model or settings.gemini_model

    def _generate(self, prompt: str) -> str:
        url = f"{self.BASE_URL}/{self.model}:generateContent"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(
            url,
            headers={"Content-Type": "application/json", "x-goog-api-key": self.api_key},
            json=payload,
        )
        response.raise_for_status()
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as e:
            raise RuntimeError(f"Unexpected Gemini response: {response.text}") from e

    def classify(self, message: str, categories: list[str]) -> str:
        prompt = (
            f"Klasifikasikan pesan ini ke salah satu kategori: {', '.join(categories)}. "
            f"Pesan: '{message}'. Jawab HANYA dengan satu kata kategori tersebut."
        )
        text = self._generate(prompt)
        return text.strip().strip(".,!").title()

    def extract_expense(self, message: str, categories: list[str]) -> dict:
        prompt = (
            f"Ekstrak data pengeluaran dari pesan ini: '{message}'. "
            f"Kategori harus salah satu dari: {', '.join(categories)}. "
            "Jawab HANYA dengan JSON valid, tanpa markdown, format persis: "
            '{"title": "...", "amount": <number>, "category": "..."}. '
            "Amount dalam Rupiah, angka murni tanpa titik/koma pemisah ribuan."
        )
        text = self._generate(prompt).strip()
        text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Gemini returned non-JSON: {text}") from e