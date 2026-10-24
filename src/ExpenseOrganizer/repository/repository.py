import json, csv
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


    def export_report(self, path: str, output_file: str, file_format: str = "csv"):
        # 1. Carregar todas as transações
        transactions = self.load(path)

        # 2. Exportar em CSV
        if file_format.lower() == "csv":
            with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                # Cabeçalho
                writer.writerow([
                    "Description",
                    "Amount",
                    "Type",
                    "Date",
                    "Time"
                ])

                # Linhas de transações
                for t in transactions:
                    writer.writerow([
                        t._description,
                        t._amount,
                        t._transaction_type,
                        t._transaction_date,
                        t._transaction_time
                    ])

        # 3. Futuro: outros formatos (json, xlsx, pdf)
        else:
            raise ValueError(f"Format '{file_format}' not supported yet")

