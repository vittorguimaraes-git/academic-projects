from datetime import datetime

class Transaction:
    def __init__(self, description: str, amount: float, transaction_type: str):
        self._amount = amount
        self._description = description
        self._transaction_type = transaction_type
        self._transaction_date = datetime.now().strftime("%Y-%m-%d")
        self._transaction_time = datetime.now().strftime("%H:%M:%S")
        self._history = []

    @property
    def amount(self):
        return self._amount

    @property
    def description(self):
        return self._description

    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, value):
        self._transaction_date = value

    @property
    def transaction_time(self):
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self._transaction_time = value

    @classmethod
    def from_dict(cls, data: dict):
        t = cls(
            description=data.get("description", ""),
            amount=data.get("amount", 0.00),
            transaction_type=data.get("transaction_type", ""),
        )
        t.transaction_date = data.get("transaction_date")
        t.transaction_time = data.get("transaction_time")
        return t


    def to_dict(self) -> dict:
        return {"description": self._description.lower(),
                "amount": self._amount,
                "transaction_type": self._transaction_type,
                "transaction_date": self._transaction_date,
                "transaction_time": self._transaction_time,
                "history": self._history
                }
