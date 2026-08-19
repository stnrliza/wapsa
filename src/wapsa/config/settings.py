import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    notion_api_key: str
    notion_notes_db_id: str
    gemini_model: str = "gemini-3.5-flash-lite"

    @classmethod
    def load(cls) -> "Settings":
        required = {
            "gemini_api_key": os.getenv("GEMINI_API_KEY"),
            "notion_api_key": os.getenv("NOTION_API_KEY"),
            "notion_notes_db_id": os.getenv("NOTION_NOTES_DB_ID"),
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise EnvironmentError(f"Missing required env vars: {missing}")
        return cls(**required)

settings = Settings.load()
