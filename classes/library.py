from classes.book import Book
from classes.User import User

class Library:
    def __init__(self, books: list[Book], users: list[User]):
        self.books = books
        self.users = users

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def list_available_books(self):
        book_list = []
        for book in self.books:
            if book.is_available:
                book_list.append(book)







