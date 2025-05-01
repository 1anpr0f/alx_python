"""create a function"""
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class (a_class).

    This function returns:
    - True if the object is an instance of a class that inherits from a_class, but not a direct
      instance of a_class itself.
    - False if the object is a direct instance of a_class or is not related to it.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if the object is an instance of a class that inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
