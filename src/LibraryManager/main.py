from LibraryManager.models.book import Book
from LibraryManager.repository.BookRepository import BookRepository
from LibraryManager.services.BookServices import BookServices
from LibraryManager.repository.UserRepository import UserRepository
from LibraryManager.models.user import User
from LibraryManager.services.UserServices import UserServices


banco = BookRepository()
users_table = UserRepository()
library = BookServices()
users = UserServices()

livro = Book(title="1984", author="George Orwell", publication_year=1949, is_available=True)
livro2 = Book(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960, is_available=False)
user1 = User(name="test", email="test@gmail.com")
user2 = User(name="test2", email="test2@gmail.com")

# users.add_user("test5", "test5@gmail.com")
# users = users_table.get_users()
# banco.save_book(livro)
# banco.save_book(livro2)
# print(banco.search_book("To Kill a Mockingbird"))

library.show_books()
print()
users.show_users()


