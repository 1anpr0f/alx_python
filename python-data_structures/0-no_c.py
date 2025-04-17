def no_c(my_string):
    new = ""
    for i in my_string:
        for j in i:
            if j != "c":
                new+=i
    return "{} \n {}" .format(new,my_string)
    
