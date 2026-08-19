from dataclasses import dataclass
from datetime import date as Date

VALID_CATEGORIES = ("Work", "Life", "Balance")

@dataclass
class Note:
    raw_text: str
    title: str
    category: str
    date: Date

    def __post_init__(self):
        if self.category not in VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {self.category}")
