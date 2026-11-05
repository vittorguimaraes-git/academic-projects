class Loan:
    def __init__(self, id: int, user_id: int, book_id: int, borrowed_at: str, returned_at: str):
        self._id = id
        self._user_id = user_id
        self._book_id = book_id
        self._borrowed_at = borrowed_at
