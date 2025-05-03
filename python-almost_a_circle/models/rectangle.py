"""use import statement __import__(file).name."""
from base import Base
class Rectangle(Base):
    """
   Rectangle class that inherits from Base.

    Args:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        x (int): x position
        y (int): y position
        id (int): ID from Base
    """
    def __init__(self,width,height,x=0,y=0,id):
        """
        Initialize a rectangle instance.
        """
        super().__init__(id)
        self.width= width
        self.height=height
        self.x =x
        self.y=y
        
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value,int):
            raise TypeError("the with must be an integer")
        self.__width=value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value,int):
            raise TypeError("the with must be an integer")
        self.__height=value
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        if value < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(value,int):
            raise TypeError("the with must be an integer")
        self.__x=value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        if value < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(value,int):
            raise TypeError("the with must be an integer")
        self.__y=value
        