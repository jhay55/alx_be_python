class Shape:
    """Base class for different shapes.
    
    This class serves as a blueprint for other shape classes.
    It is not meant to be instantiated directly.
    
    Methods:
        area: Should be implemented by subclasses to calculate the shape's area.
    """
    def __init__(self) -> None:
        raise NotImplementedError("Cannot instantiate abstract class 'Shape' directly.")
    
    def area(self) -> float:
        """Calculates the area of the shape.
        
        This method must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Represents a rectangle shape.
    
    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Methods:
        area: Calculates the area of the rectangle.
    """
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculates the area of the rectangle.
        
        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """Represents a circle shape.
    
    Attributes:
        radius (float): The radius of the circle.
    
    Methods:
        area: Calculates the area of the circle.
    """
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Calculates the area of the circle using the formula πr².
        
        Returns:
            float: The area of the circle.
        """
        import math
        return math.pi * (self.radius ** 2)

