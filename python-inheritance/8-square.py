"""import statement from 7-rectangle.py."""
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """square inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size",size)
        self.__size=size
        super().__init__(size,size)
    def area(self):
        """return the area of size"""
        return self.__size**2 
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)       