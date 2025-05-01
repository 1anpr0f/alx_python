"""create a function"""
def is_kind_of_class(obj, a_class):
    """return true if the obj is an instance of a_class that inherits 
    return false if obj is a direct instance or unrelated""" 
    if isinstance(obj,a_class) and type(obj)!=a_class:
        return True
    return False