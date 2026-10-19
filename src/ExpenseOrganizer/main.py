from ExpenseOrganizer.models.transaction import Transaction
from src.ExpenseOrganizer.models.organizer import Organizer
trasaction = Transaction(100, "comida", "expense")
trasaction2 = Transaction(300, "Trabalho", "income")
transactions = list()

manager = Organizer(transactions)

manager.add_transaction(trasaction)
manager.add_transaction(trasaction2)
manager.list_transactions(filter_transaction="expense")
manager.list_transactions(filter_transaction="income")
manager.list_transactions()
manager.show_balance()