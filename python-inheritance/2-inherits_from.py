#!/usr/bin/python3
"""Defines a function that checks for inherited class instances."""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False if obj is a direct instance or unrelated.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
