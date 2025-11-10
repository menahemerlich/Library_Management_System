
class Book:
    def __init__(self, title: str, author: str, isbn: int, is_available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def get_book_info(self):
        print(f"title: {self.title}, author: {self.author}, ISBN: {self.isbn}, is available: {self.is_available}")
