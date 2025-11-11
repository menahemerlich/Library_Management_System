from  classes.library import Library,Book, User
import json

class FileHandling:
    @staticmethod
    def guarding_json( library:Library):
        data={'books':[], 'users':[]}
        for book in library.books:
            data['books'].append(book.__dict__)
        for user in library.users:
            data['users'].append(user.__dict__)
        with open('library.json','w') as j:
            j.write(json.dumps(data))

    @staticmethod
    def rescue_from_json(file_name = 'library.json', library:Library = Library([],[])):
        try:
            with open( file_name, "r" ) as j:
                data = json.load(j)
                if len(data['books']) > 0:
                    for book in data['books']:
                        library.add_book(Book(book['title'],book[ 'author'], book['isbn'], book['is_available']))
                if len(data['users']) > 0:
                    for user in data['users']:
                        library.add_user(User(user['name'],user['id'],user['borrowed_books']))
        except FileNotFoundError:
            print("The file does not exist. Building a new directory.")
        return library
