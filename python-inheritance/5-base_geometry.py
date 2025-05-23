#!/usr/bin/python3
"""Defines the BaseGeometry class with area and integer_validator methods."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception with a message for unimplemented area."""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = name
        self.value = value
