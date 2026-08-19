from services.note_integration_service import NoteIngestionService

def main():
    service = NoteIngestionService()
    result = service.ingest(
        raw_text="besok deadline laporan praktikum jam 5 sore",
        title="Laporan Praktikum",
    )
    print("Saved:", result.get("url"))

if __name__ == "__main__":
    main()