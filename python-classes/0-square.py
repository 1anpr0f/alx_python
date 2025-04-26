#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. No type/value verification.
        """
        self.__size = size
