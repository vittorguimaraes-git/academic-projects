from LibraryManager.repository.BookRepository import BookRepository
from LibraryManager.models.book import Book

class BookServices:

    def add_book(self, title: str, author: str, publication_year: int, is_available: bool = True):
        try:

            if not title:
                raise ValueError("Title cannot be empty.")
            elif not author:
                raise ValueError("Author cannot be empty.")
            elif not isinstance(publication_year, int) or publication_year <= 0:
                raise ValueError("Publication year must be a positive integer.")

            book = Book(title=title, author=author, publication_year=publication_year, is_available=is_available)
            repository = BookRepository()
            repository.save_book(book)

        except ValueError as erro:
            print(f"Error: {erro}")

    def show_books(self):

        repository = BookRepository()
        books = repository.get_books()

        for book in books:
            if book.is_available == 1:
                book.is_available = True
            else:
                book.is_available = False

            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}, Available: {book.is_available}")


