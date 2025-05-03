"""create a class base."""
class Base:
    """create a class attribute"""
    __nb_objects = 0
    def __init__(self,id=None):
        """
        Initialize a new Base instance.

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id != None:
            self.id=id
        else:
            Base.__nb_objects+=1
            self.id=Base.__nb_objects