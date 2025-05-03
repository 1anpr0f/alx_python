"""create a class base."""
class base:
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
            base.__nb_objects+=1
            self.id=base.__nb_objects