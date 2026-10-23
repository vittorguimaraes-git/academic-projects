from ExpenseOrganizer.models.transaction import Transaction
from ExpenseOrganizer.repository.repository import TransactionRepository
from ExpenseOrganizer.models.organizer import Organizer

# 🟡 MVP 2 — Manutenção de transações (com histórico)

# - Implementar edit_transaction(id, new_data) para editar transações
#   ➡️ Mas sem perder os dados antigos:
#   - Antes de sobrescrever os campos, salvar os valores atuais em um campo "history"
#   - O "history" pode ser uma lista de dicionários dentro da transação
#   - Cada item do histórico deve registrar:
#       {"field": "amount", "old_value": 3000, "edited_at": "2026-10-22 15:50:00"}
#   - Assim, toda alteração fica rastreável e auditável
#   - Importante em sistemas financeiros: nunca apagar dados, apenas marcar correções

# - Implementar remove_transaction(id) para remover transações
#   ➡️ Decidir se a remoção será:
#   - "hard delete" (excluir de vez da lista e reescrever o JSON)
#   - ou "soft delete" (marcar a transação como removida, ex: {"deleted": True})
#   - Soft delete preserva histórico e evita perda de dados

repo = TransactionRepository()

transactions = repo.load("transactions.json")
new_transaction = Transaction("expensetest", 1000, "expense")
new_transaction2 = Transaction("incometest", 2000, "income")

organizer = Organizer(transactions)
organizer.find_by_description("edit_test", "expense")



repo.save("transactions.json", organizer.transactions)

