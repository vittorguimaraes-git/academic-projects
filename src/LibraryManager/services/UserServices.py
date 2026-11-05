from LibraryManager.repository.UserRepository import UserRepository
from LibraryManager.models.user import User


class UserServices:
    def add_user(self, user: str, email: str):
        try:

            if not isinstance(user, str) or not isinstance(email, str):
                raise TypeError("The user and email are invalid")

            elif not user:
                raise ValueError("The user field cannot be empty")

            elif not email:
                raise ValueError("The email field cannot be empty")

            user = User(user, email)
            repository = UserRepository()
            repository.save_user(user)

        except (ValueError, TypeError) as erro:
            print(f"Error: {erro}")

    def show_users(self):

        repository = UserRepository()
        users = repository.get_users()

        for user in users:
            print(f"ID: {user.id}, Name: {user.user}, Email: {user.email}")

