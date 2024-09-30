
from books import Book, Library

class Main:
    def main():
        book1 = Book()   
        book2 = Book("1984", "George Orwell")  
        book3 = Book()  

        book1.set_title("The Great Gatsby")
        book1.set_author("F. Scott Fitzgerald")
        book3.set_title("To Kill a Mockingbird")
        book3.set_author("Harper Lee")

        book1.displayBookInfo()
        book2.displayBookInfo()
        book3.displayBookInfo()
        print(f"Total number of books created: {Book.getTotalBooks()}")

        library = Library("City Library", Book.getTotalBooks())
        library.displayLibraryInfo()

Main.main()