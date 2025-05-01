"""execute file from 7-rectangle.py."""
namespace = {}
with open('7-rectangle.py','r') as file:
    code=file.read()
    exec(code,namespace)
Rectangle=namespace['Rectangle']
class Square(Rectangle):
    """square inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size",size)
        self.__size=size
        super().__init__(size,size)
    def area(self):
        """return the area of size"""
        return self.__size**2        