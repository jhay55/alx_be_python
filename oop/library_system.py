class Book:
    """Represents a general book with a title and an author.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    
    Methods:
        __str__: Returns a user-friendly string representation of the book.
        __repr__: Returns a detailed string representation of the book.
    """
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author 

    def __str__(self):
        """Provides a user-friendly string representation of the book."""
        return f'{self.__class__.__name__}: {self.title} by {self.author}'

    def __repr__(self):
        """Provides a detailed string representation of the book for debugging."""
        return f'{self.__class__.__name__}: {self.title} by {self.author}'

class EBook(Book):
    """Represents an electronic book (EBook), a subclass of Book.
    
    Attributes:
        file_size (int): The size of the eBook file in KB.
    
    Methods:
        __str__: Returns a user-friendly string representation of the eBook, including file size.
        __repr__: Returns a detailed string representation of the eBook, including file size.
    """
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = file_size   

    def __str__(self):
        """Provides a user-friendly string representation of the eBook."""
        return f'{super().__str__()}, File Size: {self.file_size}KB'

    def __repr__(self):
        """Provides a detailed string representation of the eBook for debugging."""
        return f'{super().__repr__()}, File Size: {self.file_size}KB'
    
class PrintBook(Book):
    """Represents a printed book, a subclass of Book.
    
    Attributes:
        page_count (int): The number of pages in the book.
    
    Methods:
        __str__: Returns a user-friendly string representation of the printed book, including page count.
        __repr__: Returns a detailed string representation of the printed book, including page count.
    """
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Provides a user-friendly string representation of the printed book."""
        return f'{super().__str__()}, Page Count: {self.page_count}'

    def __repr__(self):
        """Provides a detailed string representation of the printed book for debugging."""
        return f'{super().__repr__()}, Page Count: {self.page_count}'

class Library:
    """Represents a library that can store a collection of books.
    
    Attributes:
        name (str): The name of the library.
        books (list): A list to store book instances.
    
    Methods:
        add_book: Adds a book to the library if it is not already present.
        list_books: Lists all the books in the library.
    """
    def __init__(self, name_of_library: str = "") -> None:
        self.name = name_of_library
        self.books = []  # Changed to an instance attribute

    def add_book(self, book: Book) -> None:
        """Adds a book to the library collection if it is not already present.
        
        Args:
            book (Book): The book to add to the library.
        """
        if book not in self.books:
            self.books.append(book)

    def list_books(self) -> None:
        """Prints all the books currently in the library collection."""
        if self.books:
            for item in self.books:
                print(item)
        else:
            print("The library is currently empty.")
