class Book:
    def __init__(self, title: str, author: str, publication_year: int, is_available: bool):
        self._id = None
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._is_available = is_available

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def publication_year(self):
        return self._publication_year

    @property
    def is_available(self):
        return self._is_available

    @id.setter
    def id(self, value: int):
        self._id = value

    @is_available.setter
    def is_available(self, value: bool):
        self._is_available = value


