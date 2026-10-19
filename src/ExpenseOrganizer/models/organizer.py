from typing import Optional, List
from src.ExpenseOrganizer.models.transaction import Transaction
from src.ExpenseOrganizer.helpers.functions import show_transaction, show_balance


class Organizer:

    def __init__(self, transactions: Optional[List[Transaction]] = None):
        self._transactions = transactions or []

    def add_transaction(self, trasaction: Transaction) -> None:
        self._transactions.append(trasaction)

    def list_transactions(self, filter_transaction: Optional[str] = None) -> None:
        transactions = self._get_transactions(filter_transaction)
        if not transactions:
            print(f"There are 0 {filter_transaction or ''} transactions")
        else:
            for t in transactions:
                show_transaction(t)

    def show_balance(self) -> None:
        show_balance(self._calculate_balance())


    def _get_transactions(self, filter_transaction: Optional[str] = None):
        if filter_transaction is None:
            return self._transactions
        if filter_transaction not in ["income", "expense"]:
            raise ValueError("Invalid filter type, did you mean 'income' or 'expense'?")
        return [transaction for transaction in self._transactions if transaction.trasaction_type == filter_transaction]

    def _calculate_balance(self) -> float:
        balance = 0
        for trasaction in self._transactions:
            if trasaction.trasaction_type == "income":
                balance += trasaction.amount
            else:
                balance -= trasaction.amount

        return balance
