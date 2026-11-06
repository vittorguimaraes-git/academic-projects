import sqlite3
from LibraryManager.models.loan import Loan



class LoanRepository:
    def add_loan(self, obj: Loan):
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                        """
                                INSERT INTO loans
                                (user_id, book_id, borrowed_at)
                                VALUES (?, ?, ?)
                            """,
                            (obj.user_id, obj.book_id, obj.borrowed_at)
                        )
            conn.commit()

    def search_book(self, book_id: str):
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM books 
                WHERE id = ?
                """, (book_id,)
            )
            conn.commit()

    def get_active_loans(self):

        with sqlite3.connect("library.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM loans WHERE returned_at is NULL""")
            rows = cursor.fetchall()
            return rows



