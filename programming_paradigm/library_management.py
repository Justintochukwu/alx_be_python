class book:
    def __init__(self, title, author):
        self.books = title
        self.author = author
        self._is_checked_out = False
    
    def check_out_book(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f'"{self.title}" is already checked out.')
        
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f'"{self.title}" was not checked out.')
    
    def is_available(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f'Book titled "{title}" not found in the library.')
        
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f'Book titled "{title}" not found in the library.')
        
    def list_available_books(self):
        for books in self._books:
            if book.is_available():
                print(f'{book.title} by {book.author}')
                
                