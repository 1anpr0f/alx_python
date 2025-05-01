"""create a function"""
def is_kind_of_class(obj, a_class):
    """retrun true if the objwct is an instance of a clsaa that inherits
    retrun false if object is direct intanse or unrelated"""
    if isinstance(obj,a_class) and type(obj)!=a_class:
        return True
    return False