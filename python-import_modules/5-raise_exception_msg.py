def raise_exception_msg(message=""):
    if not isinstance(message,str):
        raise TypeError("an error occured")
    print(message)