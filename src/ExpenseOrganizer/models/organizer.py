from datetime import datetime
from typing import Optional, List
from src.ExpenseOrganizer.models.transaction import Transaction
from src.ExpenseOrganizer.helpers.functions import format_transactions, format_balance, format_report


class Organizer:
    def __init__(self, transactions: Optional[List[Transaction]] = None):
        self._transactions = transactions or []

    @property
    def transactions(self) -> List[Transaction]:
        return self._transactions

    def add_transaction(self, transaction: Transaction) -> None:

        if transaction.amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if transaction.transaction_type not in ["income", "expense"]:
            raise ValueError("Transaction type must be either 'income' or 'expense'")

        self._transactions.append(transaction)

    def show_transactions(self, filter_transaction_type: Optional[str] = None) -> None:
        format_transactions(self._get_dict_transactions(), filter_transaction_type)

    def show_balance(self) -> None:
        format_balance(self._get_balance())

    def show_monthly_report(self, year: Optional[str|int] = None, month: Optional[str|int] = None ):
        if year is None:
            year = datetime.now().year
        if month is None:
            month = datetime.now().month

        format_report(self._get_dict_transactions(), year, month)

    def find_by_description(self, desc: str) -> List[Transaction]:
        return [
            t for t in self._transactions if t.description in desc
        ]

    def _get_dict_transactions(self):
        return [
            t.to_dict() for t in self._transactions
        ]

    def _get_balance(self) -> float:
        income = sum([t.amount for t in self._transactions])
        expense = sum([t.amount for t in self._transactions])

        return income + expense