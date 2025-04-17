def no_c(my_string):
    new = ""
    for i in my_string:
        for j in i:
            if j != "c" or j != "C":
                new+=i
    return new