"""create a function"""
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class) and type(obj) != a_class
    

