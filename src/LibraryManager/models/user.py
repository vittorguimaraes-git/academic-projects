class User:
    def __init__(self, name: str, email: str):
        self._id = None
        self._user = name
        self._email = email

    @property
    def user(self):
        return self._user

    @property
    def email(self):
        return self._email

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
