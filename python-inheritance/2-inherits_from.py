"""create a function"""
def is_kind_of_class(obj, a_class):
    """ return true if object isinstance of subclass.
    
    else return false
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
    

