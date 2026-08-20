from datetime import date
from wapsa.clients.gemini_client import GeminiClient
from wapsa.clients.notion_client import NotionClient
from wapsa.models.expense import Expense, VALID_EXPENSE_CATEGORIES
from wapsa.config.settings import settings

class ExpenseIngestionService:
    def __init__(self):
        self.gemini = GeminiClient()
        self.notion = NotionClient()

    def ingest(self, raw_text: str, source: str = "Cash") -> dict:
        extracted = self.gemini.extract_expense(raw_text, list(VALID_EXPENSE_CATEGORIES))

        category = extracted.get("category", "Other")
        if category not in VALID_EXPENSE_CATEGORIES:
            category = "Other"

        expense = Expense(
            raw_text=raw_text,
            title=extracted.get("title", raw_text[:50]),
            amount=float(extracted.get("amount", 0)),
            category=category,
            date=date.today(),
            source=source,
        )
        return self.notion.create_expense(settings.notion_expense_db_id, expense)