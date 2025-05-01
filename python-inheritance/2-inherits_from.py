"""create a function."""
def is_kind_of_class(obj, a_class):
    
    """
    Determine if an object is an instance of a subclass of the specified class.

    This function returns True if `obj` is an instance of a class that inherits
    (directly or indirectly) from `a_class`, but is not a direct instance of `a_class`.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to compare inheritance against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class`, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class


