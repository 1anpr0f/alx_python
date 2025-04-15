def safe_print_division(a, b):
    try:
        result = a/b 
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("{:d} / {:d} = {}".format(a,b,result))
