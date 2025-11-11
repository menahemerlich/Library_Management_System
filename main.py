from classes.library import Library
from classes.book import Book
from classes.User import User


my_library = Library([], [])
def menu():
    while True:
        print("===menu===\n"
              "1. Add book\n"
              "2. Add user\n"
              "3. Borrow book\n"
              "4. Return book\n"
              "5. Get a list of available books\n"
              "6. Search for a book\n"
              "7. Save & Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            isbn = int(input("Enter the ISBN: "))
            my_library.add_book(Book(title, author, isbn))
            print("The book was added successfully.")
        elif choice == "2":
            name = input("Enter your name: ")
            user_id = int(input("Enter your user_ID: "))
            my_library.add_user(User(name, user_id))
            print("User added successfully")
        elif choice == "3":
            user_id = int(input("Enter your user_ID: "))
            book_isbn = int(input("Enter the book_ISBN: "))
            if my_library.borrow_book(user_id, book_isbn):
                print("The book was loaned to the user.")
            else:
                print("One of the entered data is incorrect.")
        elif choice == "4":
            user_id = int(input("Enter your user_ID: "))
            book_isbn = int(input("Enter the book_ISBN: "))
            if my_library.return_book(user_id, book_isbn):
                print("The book was returned to the library.")
            else:
                print("One of the entered data is incorrect.")
        elif choice == "5":
            print("List of available books:")
            my_library.list_available_books()
        elif choice == "6":
            search_type = input("How do you want to search? By title/author/ISBN ?")
            search_word = input("What is your search term? ")
            my_library.search_book(search_type, search_word)
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice, try again.")

menu()
