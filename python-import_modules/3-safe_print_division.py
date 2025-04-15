def safe_print_division(a, b):
    try:
        result = a/b 
        return result
    except ValueError:
        print("an error occured")
    finally:
        print("{:d} / {:d} = {}".format(a,b,result))
safe_print_division()
