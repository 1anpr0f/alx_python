"""create a function"""
def is_kind_of_class(obj, a_class):
    """check if abject is instnace of class
    or instunce of its subclass and return true
    else return false"""
    if isinstance(obj,a_class):
        return True
    return False