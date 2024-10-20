class Book:
    """Represents a book with a title, author, and year of publication.
    
    To create an instance:
        Book(title, author, year)
    
    Example:
        book = Book('The Fellowship of the Ring', 'J.R.R. Tolkien', 1954)
    
    Note:
        This class does not validate the input data.
    
    Methods:
        __str__: Returns a formatted string for user-friendly display.
        __repr__: Returns a detailed string for debugging and development.
        __del__: Notifies when a book instance is deleted.
    """
    
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.author}, published in {self.year}'
    
    def __repr__(self):
        return f'Book(\'{self.title}\', \'{self.author}\', {self.year})'
    
    def __del__(self):
        print(f'Deleting {self.title}')
