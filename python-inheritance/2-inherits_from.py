"""create a function"""
def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of a class that inherits
    from the specified class (a_class), either directly or indirectly.

    Return False if the object is a direct instance of a_class or is unrelated.
    """
    return isinstance(obj, a_class) and type(obj) != a_class