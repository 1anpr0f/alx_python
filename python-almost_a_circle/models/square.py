"""import from rectangle"""
from models.rectangle import Rectangle
"""
create class square that inherits from rectangle    
"""
class square(Rectangle):
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
        super().__init__(size,x,y,id)
    def __str__ (self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        
        
