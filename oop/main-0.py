from library_system import Book, Ebook, PrintBook, Library

def main():
    my_library = Library()
    
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = Print_novel = Print("The Catcherin the Rye", "J.D Salinger", 234)
    my_lirary.add_book(classiic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)
    
    my_library.list_books()
    
if __name__ == "__main)__":
    main()