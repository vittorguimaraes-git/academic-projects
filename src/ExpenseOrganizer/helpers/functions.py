import locale
from typing import Optional, List

def format_currency(value: float) -> str:
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    return locale.currency(value, symbol=True, grouping=True)


def format_balance(balance: float) -> None:
    print(f"Balance: {format_currency(balance)}")


def format_transactions(transactions: List[dict], filter_transactions: Optional[str] = None) -> None:
    if filter_transactions is not None:
        if filter_transactions not in ["income", "expense"]:
            raise ValueError("filter_transactions should be either 'income' or 'expense'")
    if not transactions:
        print("No transactions found")
        return None
    for transaction in transactions:
        if not filter_transactions or filter_transactions == transaction["transaction_type"]:
            print(f"Type: {transaction['transaction_type'].title()}\n"
                  f"Value: {format_currency(transaction['amount'])}\n"
                  f"Description: {transaction['description'].title()}\n")
    return None