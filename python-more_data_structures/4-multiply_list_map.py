def multiply_list_map(my_list=[], number=0):
    results = map(lambda x:x * number,my_list)
    return list(results)