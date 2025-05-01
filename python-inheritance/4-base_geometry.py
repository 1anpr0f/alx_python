"""create a class BaseGeometry."""
class BaseGeometry:
    """A base class for geometric shapes."""
    def __init__(self):
        """Raises an exception with a message for unimplemented area."""
        raise Exception("area() is not implemented")
        