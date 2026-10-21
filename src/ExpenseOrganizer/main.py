from ExpenseOrganizer.models.transaction import Transaction
from ExpenseOrganizer.models.organizer import Organizer


trasaction = Transaction("Mercado", 400, "expense")
trasaction2 = Transaction("Trabalho", 1000, "income")
transactions = [trasaction, trasaction2]

manager = Organizer(transactions)
manager.add_transaction("Churrasco", 400, "expense")
manager.show_transactions(filter_transaction="expense")
manager.show_transactions(filter_transaction="income")
manager.show_balance()
