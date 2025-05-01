#!/usr/bin/python3
"""Defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class.

    The function returns True only if obj is an instance of a class that
    inherits from a_class (directly or indirectly), but not if obj is a direct
    instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The reference class.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
