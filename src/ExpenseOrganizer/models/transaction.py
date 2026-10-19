class Transaction:
    def __init__(self, amount: float, description: str, transaction_type: str):

        if amount <= 0:
            raise ValueError

        if not description:
            raise ValueError

        if transaction_type not in ['income', 'expense']:
            raise ValueError

        self._amount = amount
        self._description = description
        self._trasaction_type = transaction_type

    @property
    def amount(self):
        return self._amount

    @property
    def description(self):
        return self._description

    @property
    def trasaction_type(self):
        return self._trasaction_type