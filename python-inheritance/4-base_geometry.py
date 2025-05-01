#!/usr/bin/python3
"""Defines the BaseGeometry class with an area method."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception with a message for unimplemented area."""
        for attr in area(self):
            if not attr.startswith('__') or attr == 'area':
                raise Exception("area() is not implemented")
        
