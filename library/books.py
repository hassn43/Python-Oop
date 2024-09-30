
class Book:
    totalBooks = 0  

    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title
        self.author = author
        Book.totalBooks += 1

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def getTotalBooks():
        return Book.totalBooks

    def displayBookInfo(self):
        print(f"Title: {self.title}, Author: {self.author}")




class Library:
    def __init__(self, libraryName="Unnamed Library", numberOfBooks=0):
        self.libraryName = libraryName
        self.numberOfBooks = numberOfBooks

    def get_libraryName(self):
        return self.libraryName

    def set_libraryName(self, libraryName):
        self.libraryName = libraryName

    def get_numberOfBooks(self):
        return self.numberOfBooks

    def set_numberOfBooks(self, numberOfBooks):
        self.numberOfBooks = numberOfBooks

    def displayLibraryInfo(self):
        print(f"Library Name: {self.libraryName}, Number of Books: {self.numberOfBooks}")
        
