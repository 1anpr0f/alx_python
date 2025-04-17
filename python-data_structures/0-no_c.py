def no_c(my_string):
    new = ""
    for i in my_string:
        for j in i:
            if j != "c" and j != "C":
                new+=i
    return "{}" .format(new)
    
