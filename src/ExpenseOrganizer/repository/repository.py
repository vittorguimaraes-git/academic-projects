import json
from typing import List
from ExpenseOrganizer.models.transaction import Transaction

class TransactionRepository:
    def load(self, path) -> List[Transaction]:
        with open(path, "r") as f:
            data = json.load(f)
        return [
            Transaction.from_dict(item) for item in data
        ]

    def save(self, path: str, transactions: List[Transaction]):
        with open(path, "w", encoding= "utf-8") as f:
            json.dump([t.to_dict() for t in transactions], f, indent=4, ensure_ascii=False)


