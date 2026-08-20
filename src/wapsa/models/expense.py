from dataclasses import dataclass
from datetime import date as Date

VALID_EXPENSE_CATEGORIES = (
    "Food", "Transport", "Bills", "Shopping", "Health", "Entertainment", "Other"
)
VALID_SOURCES = ("Cash", "E-wallet", "Bank")

@dataclass
class Expense:
    raw_text: str
    title: str
    amount: float
    category: str
    date: Date
    source: str = "Cash"

    def __post_init__(self):
        if self.category not in VALID_EXPENSE_CATEGORIES:
            raise ValueError(f"Invalid category: {self.category}")
        if self.source not in VALID_SOURCES:
            raise ValueError(f"Invalid source: {self.source}")
        if self.amount <= 0:
            raise ValueError(f"Amount must be positive: {self.amount}")