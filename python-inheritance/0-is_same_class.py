"""create function"""
def is_same_class(obj, a_class):
    """check if function is exact 
    instance of a class and return true else 
     return false"""
    if type(obj) == a_class:
        return True
    return False