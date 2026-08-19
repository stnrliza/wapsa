from __future__ import annotations

import requests
from typing import Optional
from wapsa.config.settings import settings
from wapsa.models.note import Note

class NotionClient:
    BASE_URL = "https://api.notion.com/v1"
    NOTION_VERSION = "2022-06-28"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.notion_api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": self.NOTION_VERSION,
        }

    def create_note(self, database_id: str, note: Note) -> dict:
        payload = {
            "parent": {"database_id": database_id},
            "properties": {
                "Title": {"title": [{"text": {"content": note.title}}]},
                "Category": {"select": {"name": note.category}},
                "Raw Text": {"rich_text": [{"text": {"content": note.raw_text}}]},
                "Date": {"date": {"start": note.date.isoformat()}},
            },
        }
        response = requests.post(f"{self.BASE_URL}/pages", headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
