from wapsa.services.expense_integration_service import ExpenseIngestionService

def main():
    service = ExpenseIngestionService()
    result = service.ingest("beli kopi di indomaret 25rb pake e-wallet", source="E-wallet")
    print("Saved:", result.get("url"))

if __name__ == "__main__":
    main()