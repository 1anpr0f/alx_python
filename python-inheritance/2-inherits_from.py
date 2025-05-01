"""create a function"""
def is_kind_of_class(obj, a_class):
    """
    Determine whether an object is an instance of a subclass of a specified class.

    This function returns True if the object is an instance of a class that inherits 
    (either directly or indirectly) from the specified class `a_class`, but not if the 
    object is a direct instance of `a_class` itself.

    Args:
        obj (Any): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class` (excluding direct instances),
              False otherwise.

    Example:
        >>> class Animal: pass
        >>> class Dog(Animal): pass
        >>> is_kind_of_class(Dog(), Animal)
        True
        >>> is_kind_of_class(Animal(), Animal)
        False
    """
    return isinstance(obj, a_class) and type(obj) != a_class

