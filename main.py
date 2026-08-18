import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.5-flash-lite"

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

payload = {
    "contents": [
        {
            "parts": [
                {"text": "Klasifikasikan pesan ini ke salah satu kategori: kerja, kuliah, harian. Pesan: 'besok deadline laporan praktikum jam 5 sore'. Jawab cuma dengan satu kata kategori."}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print("Status:", response.status_code)
print(response.json())