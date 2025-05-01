#!/usr/bin/python3
"""Defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or inherits from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
