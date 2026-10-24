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
            print(f"Date {transaction['transaction_date'].replace("-", "/")} | {transaction['transaction_time']}\n"
                  f"Type: {transaction['transaction_type'].title()}\n"
                  f"Value: {format_currency(transaction['amount'])}\n"
                  f"Description: {transaction['description'].title()}\n")
    return None


def format_report(reports: List[dict], year: Optional[str|int] = None, month: Optional[str|int] = None) -> None:
    date = f"{year}-{month}"
    monthly_transactions = [
        t for t in reports if t["transaction_date"].startswith(date)
    ]
    monthly_income = sum(t["amount"] for t in monthly_transactions if t["transaction_type"] == "income")
    monthly_expense = sum(t["amount"] for t in monthly_transactions if t["transaction_type"] == "expense")
    monthly_balance = monthly_income - monthly_expense
    format_transactions(monthly_transactions)
    print(f"Monthly Balance: {format_currency(monthly_balance)}")

