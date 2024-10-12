# library_management.py

class Book:
    """Represents a book with a title, an author, and a checked-out status."""
    
    def __init__(self, title: str, author: str):
        """Initializes a book with a title, an author, and sets its checked-out status to False."""
        self.title = title  # Public attribute for the book's title
        self.author = author  # Public attribute for the book's author
        self._is_checked_out = False  # Private attribute to track if the book is checked out (default is False)

    def check_out(self):
        """Marks the book as checked out if it is not already checked out."""

        if not self._is_checked_out:  # If the book is not checked out, allow it to be checked out
            self._is_checked_out = True
            return True  
        return False  

    def return_book(self):
        """Marks the book as available if it was checked out."""

        if self._is_checked_out:  # If the book is checked out, allow it to be returned
            self._is_checked_out = False
            return True  
        return False  

    def is_available(self):
        """Returns True if the book is available (not checked out)"""
        return not self._is_checked_out 


class Library:
    """Represents a library that stores books and manages check-outs and returns."""
    
    def __init__(self):
        """Initializes an empty library with no books."""
        self._books = []  # Private list to store books in the library

    def add_book(self, book: Book):
        """Adds a new book to the library."""
        self._books.append(book)  # Appends the given book object to the list of books

    def check_out_book(self, title: str):
        """Finds a book by title and checks it out if it is available."""
        for book in self._books:  
            if book.title == title:  
                if book.check_out(): 
                    print(f'{book.title} by {book.author} has been checked out.')
                else:
                    print(f'{book.title} is already checked out.')
                return  
        print(f'The book titled "{title}" is not available in the library.')  

    def return_book(self, title: str):
        """Finds a book by title and returns it if it is checked out."""
        for book in self._books:  
            if book.title == title:  
                if book.return_book():  
                    print(f'{book.title} by {book.author} has been returned.')
                else:
                    print(f'{book.title} was not checked out.')
                return  
        print(f'The book titled "{title}" is not available in the library.') 

    def list_available_books(self):
        """Lists all books that are currently available (not checked out)."""
        available_books = [book for book in self._books if book.is_available()]  
        if available_books:  
            # print("Available books:")
            for book in available_books:  
                print(f'{book.title} by {book.author}')
        else:
            print("No books are available.") 
