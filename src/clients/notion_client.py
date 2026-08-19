import requests
from config.settings import settings
from models.note import Note
from models.expense import Expense

class NotionClient:
    BASE_URL = "https://api.notion.com/v1"
    NOTION_VERSION = "2022-06-28"

    def __init__(self, api_key: str = None):
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

    def create_expense(self, database_id: str, expense: Expense) -> dict:
        payload = {
            "parent": {"database_id": database_id},
            "properties": {
                "Title": {"title": [{"text": {"content": expense.title}}]},
                "Amount": {"number": expense.amount},
                "Category": {"select": {"name": expense.category}},
                "Source": {"select": {"name": expense.source}},
                "Raw Text": {"rich_text": [{"text": {"content": expense.raw_text}}]},
                "Date": {"date": {"start": expense.date.isoformat()}},
            },
        }
        response = requests.post(f"{self.BASE_URL}/pages", headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()