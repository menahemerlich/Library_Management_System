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

    def borrow_book(self,user_id, book_isbn):
        for index,user in enumerate(self.users):
            if user.id == user_id:
                for book  in self.books:
                    if book.isbn == book_isbn:
                        if book.is_available:
                            book.is_available = False
                            self.users[index].borrowed_books.append(book)

    def return_book(self,user_id, book_isbn):
        for book in self.books:
            if book_isbn == book.isbn:
                for user in self.users:
                    if user_id == user.id:
                        book.is_available = True
                        user.borrowed_books.remove(book)



   








