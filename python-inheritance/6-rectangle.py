"""read the file from 5-base_geometry.py"""
with open('5-base_geometry.py','r') as file:
    code=file.read()
    exec(code)

class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height, validates them."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return f"[Rectangle] {self.__width} - {self.__height}"
