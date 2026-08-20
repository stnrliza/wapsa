from datetime import date
from wapsa.clients.gemini_client import GeminiClient
from wapsa.clients.notion_client import NotionClient
from wapsa.models.note import Note, VALID_CATEGORIES
from wapsa.config.settings import settings

class NoteIngestionService:
    def __init__(self):
        self.gemini = GeminiClient()
        self.notion = NotionClient()

    def ingest(self, raw_text: str, title: str) -> dict:
        category = self.gemini.classify(raw_text, list(VALID_CATEGORIES))
        if category not in VALID_CATEGORIES:
            category = "Work"  # fallback default
        note = Note(raw_text=raw_text, title=title, category=category, date=date.today())
        return self.notion.create_note(settings.notion_notes_db_id, note)
