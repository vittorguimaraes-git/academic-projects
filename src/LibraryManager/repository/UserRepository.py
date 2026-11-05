import sqlite3
from LibraryManager.models.user import User


class UserRepository:
    def save_user(self, obj:User):
        with sqlite3.connect("library.db") as conn:
            print("Connected to the database successfully.")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE
                )
            """)
            cursor.execute(
                """
                INSERT INTO users
                (name, email)
                VALUES (?, ?)
                """,
                (obj.user, obj.email)
            )
            conn.commit()

    def get_users(self):
        with sqlite3.connect("library.db") as conn:
            print("Connected to the database successfully.")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE
                )
            """)
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            users = list()

            for row in rows:
                user = User(name=row[1], email=row[2])
                user.id = row[0]
                users.append(user)

            return users
