class Transaction:
    def __init__(self, description: str, amount: float, transaction_type: str):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if not description:
            raise ValueError("Description cannot be empty")

        if transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'")

        self._amount = amount
        self._description = description
        self._transaction_type = transaction_type

    @property
    def amount(self):
        return self._amount

    @property
    def description(self):
        return self._description

    @property
    def transaction_type(self):
        return self._transaction_type

    def to_dict(self) -> dict:
        return {"description": self._description,
                "amount": self._amount,
                "transaction_type": self._transaction_type}