def no_c(my_string):
    new = ""
    for i in my_string.lower():
        for j in i:
            if j != "c":
                new+=i
    return new