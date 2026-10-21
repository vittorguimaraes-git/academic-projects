from typing import Optional, List
from src.ExpenseOrganizer.models.transaction import Transaction
from src.ExpenseOrganizer.helpers.functions import format_transactions, format_balance


class Organizer:

    def __init__(self, transactions: Optional[List[Transaction]] = None):
        self._transactions = transactions or []

    def add_transaction(self, desc: str, amount: float, transaction_type: str) -> None:
        transaction = Transaction(desc, amount, transaction_type)
        self._transactions.append(transaction)

    def show_transactions(self, filter_transaction: Optional[str] = None) -> None:
        format_transactions(self._get_dict_transactions(), filter_transaction)

    def show_balance(self) -> None:
        format_balance(self._get_balance())

    def _get_dict_transactions(self):
        return [t.to_dict() for t in self._transactions]

    def _get_balance(self) -> float:
        balance = 0
        for trasaction in self._transactions:
            if trasaction.transaction_type == "income":
                balance += trasaction.amount
            else:
                balance -= trasaction.amount
        return balance






