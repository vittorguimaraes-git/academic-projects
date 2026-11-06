from typing import Optional


class Loan:
    def __init__(self, user_id: int, book_id: int, borrowed_at, returned_at: Optional[str] = None):
        self._id = None
        self._user_id = user_id
        self._book_id = book_id
        self._borrowed_at = borrowed_at
        self._returned_at = returned_at

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def borrowed_at(self):
        return self._borrowed_at

    @property
    def returned_at(self):
        return self._returned_at
