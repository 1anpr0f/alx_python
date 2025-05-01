#!/usr/bin/python3
"""Defines the BaseGeometry class with an area method."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception with a message for unimplemented area."""
        raise Exception("area() is not implemented")
if __name__ == "__main__":
    bg=BaseGeometry()
    if isinstance (bg,BaseGeometry):
        attributes = [attr for attr in dir(bg) if not attr.startswith('__') or attr == 'area']
        print(attributes)
        
        try:
            bg.area()
        except Exception as e:
            print("[{}] {}".format(type(e).__name__, e))
     
