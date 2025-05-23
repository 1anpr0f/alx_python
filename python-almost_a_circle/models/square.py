"""import from rectangle"""
from models.rectangle import Rectangle
"""
create class square that inherits from rectangle    
"""
class Square(Rectangle):
    """
    class instance
    Args:
        size(int):size of square
        x (int): The x-coordinate of the rectangle. Must be >= 0.
        y (int): The y-coordinate of the rectangle. Must be >= 0.
        id (int): Inherited from Base, unique identifier for each instance.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): Horizontal position. Defaults to 0.
            y (int, optional): Vertical position. Defaults to 0.
            id (int, optional): Unique ID. If None, an auto-incremented ID is used.

        pass
        """
        super().__init__(size,size,x,y,id)
    @property
    def size(self):
        return self.width
    @size.setter
    def size(self,value):
        """
        Setter for size: sets both width and height.
        
        """
        if self.width != self.height:
            raise ValueError("both must be equal")
        self.width=value
        self.height=value
    def __str__ (self):
        
        """String representation of the Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        
        
