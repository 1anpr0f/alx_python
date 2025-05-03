#!/usr/bin/python3
"""
Rectangle module that defines the Rectangle class, inheriting from Base.
"""
from models.base import Base



class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    Manages the dimensions and position of a rectangle shape.

    Attributes:
        width (int): The width of the rectangle. Must be >= 0.
        height (int): The height of the rectangle. Must be >= 0.
        x (int): The x-coordinate of the rectangle. Must be >= 0.
        y (int): The y-coordinate of the rectangle. Must be >= 0.
        id (int): Inherited from Base, unique identifier for each instance.
    """

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): Horizontal position. Defaults to 0.
            y (int, optional): Vertical position. Defaults to 0.
            id (int, optional): Unique ID. If None, an auto-incremented ID is used.

        Raises:
            TypeError: If width, height, x, or y are not integers.
            ValueError: If width, height, x, or y are negative.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
       
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
       
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x position attribute.

        Returns:
            int: The x position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x position attribute.

        Args:
            value (int): New x-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
       
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y position attribute.

        Returns:
            int: The y position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y position attribute.

        Args:
            value (int): New y-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """
        calculate area of the rectangle
        
        Returns:
            float:area of the rectangle
        """
        return self.__height * self.__width
    def display(self):
        """print output of # in the multiple of width 
        """
        line = '#'*self.__width
        for _ in range(self.__height):
            print(line)
    def __str__(self):
        """
        printing out a string output
        """
        return f"[Rectangle]{id}{self.__x}/{self.__y}-{self.__width}/{self.__height}"
        
        
if __name__ == "__main__":


    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)