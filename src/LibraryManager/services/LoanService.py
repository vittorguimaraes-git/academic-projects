import sqlite3, datetime
from LibraryManager.models.loan import Loan
from LibraryManager.repository.LoanRepository import LoanRepository


class LoanService:
    def borrow_book(self, user_id: str, book_id: str, borrowed_at: str):
        try:
            with sqlite3.connect("library.db") as conn:
                print("Connected to the database successfully.")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE id = ?",(user_id,))
                if cursor.fetchone() is None:
                    raise ValueError("User not found.")

                cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
                row = cursor.fetchone()
                if row is None:
                    raise ValueError("Book not found.")
                elif row[4] == 0:
                    raise ValueError("Book not available.")

                repository = LoanRepository()
                borrow_date = datetime.datetime.strptime(borrowed_at, "%Y-%m-%d").date()
                loan = Loan(user_id=int(user_id), book_id=int(book_id), borrowed_at=borrow_date)
                repository.add_loan(loan)
                cursor.execute("UPDATE books SET is_available = 0 WHERE id = ?", (book_id,))

        except ValueError as erro:
            print(f"Error: {erro}")

    def return_book(self, user_id: str, book_id:str, returned_at: str):
        try:
            with sqlite3.connect("library.db") as conn:
                print("Connected to the database successfully.")
                cursor = conn.cursor()
                cursor.execute(
                    """
                        SELECT * FROM books 
                        WHERE id = ? AND is_available = 0            
                        """, (book_id,))

                row = cursor.fetchone()
                returned_date = datetime.datetime.strptime(returned_at, "%Y-%m-%d").date()
                if row is None:
                    raise ValueError("Book not found.")

                cursor.execute(
                    """
                    UPDATE books 
                    SET is_available = 1 
                    WHERE id = ?
                    """, (book_id,)
                )

                cursor.execute(
                    """
                    UPDATE loans 
                    SET returned_at = ? 
                    WHERE book_id = ? 
                    AND user_id = ?
                    """, (returned_date, book_id, user_id)
                )
        except ValueError as erro:
            print(f"Error: {erro}")


    def show_loans(self, rows: sqlite3.Row):
        try:
            if not rows:
                raise ValueError("No active loans.")
            for row in rows:
                print(
                    f"ID: {row['id']}, User ID: {row['user_id']}, Book ID: {row['book_id']}, Borrowed at: {row['borrowed_at']}")
        except ValueError as erro:
            print(f"Error: {erro}")











