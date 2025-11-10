from classes import book,User

class Library:
    def __init__(self, books:list, users:list):
        self.books = books
        self.users = users

    def borrow_book(self,user_id, book_isbn):
        for index,user in enumerate(self.users):
            if user.id == user_id:
                for book  in self.books:
                    if book.isbn == book_isbn:
                        if book.is_available:
                            book.is_available = False
                            self.users[index].borrowed_books.append(book)

    def return_book(self,user_id, book_isbn):
        for b in self.books:
            if book_isbn == b.isbn:
                for u in self.users:
                    if user_id == u.id:
                        b.is_available = True
                        u.borrowed_books.remove(b)



