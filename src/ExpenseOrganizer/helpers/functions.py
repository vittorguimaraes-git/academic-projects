import locale
from src.ExpenseOrganizer.models.transaction import Transaction

def show_transaction(type_trasaction: Transaction) -> None:
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    print(f"Type: {type_trasaction.trasaction_type.title()}\n"
          f"Value: {locale.currency(type_trasaction.amount, symbol=True, grouping=True)}\n"
          f"Description: {type_trasaction.description.title()}\n")

def show_balance(balance: float) -> None:
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    print(f"Current balance: {locale.currency(balance, symbol=True, grouping=True)}")