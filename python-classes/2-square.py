#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with size validation and area computation."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        if not isinstance(value,int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The computed area of the square (size squared).
        """
        return self.__size ** 2
