#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. No type/value verification.
        """
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("it must be greater than zero")
        self.__size = size
