from ExpenseOrganizer.models.transaction import Transaction
from ExpenseOrganizer.repository.repository import TransactionRepository
from ExpenseOrganizer.models.organizer import Organizer

repo = TransactionRepository()

transactions = repo.load("transactions.json")
new_transaction = Transaction("expensetest", 1000, "expense")
new_transaction2 = Transaction("remove_test", 2000, "income")
organizer = Organizer(transactions)
# organizer.add_transaction(new_transaction)
# organizer.edit_transaction(parameters)
# organizer.remove_transactions(parameters)





repo.save("transactions.json", organizer.transactions)
# repo.export_report("transactions.json", "reports.csv")

