import sqlite3
from LibraryManager.models.book import Book


class BookRepository:

    def save_book(self, obj: Book):
        with sqlite3.connect("library.db") as conn:
            print("Connected to the database successfully.")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL
                    publication_year INTEGER
                    is_available BOOLEAN
                )
            """)
            cursor.execute(
                """
                INSERT INTO books
                (title, author, publication_year, is_available)
                VALUES (?, ?, ?, ?)
                """,
                (obj.title, obj.author, obj.publication_year, obj.is_available)
            )
            conn.commit()

    def get_books(self):
        with sqlite3.connect("library.db") as conn:
            print("Connected to the database successfully.")
            cursor = conn.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                author TEXT NOT NULL,
                                publication_year INTEGER,
                                is_available BOOLEAN
                            )
                        """)
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            books = list()

            for row in rows:
                book = Book(title=row[1], author=row[2], publication_year=row[3], is_available=row[4])
                book.id = row[0]
                books.append(book)

            return books

    def search_book(self, title):
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM books WHERE title = ?",
                (title,)
            )

            return cursor.fetchone()



