def no_c(my_string):
    new = ""
    for i in my_string:
        for j in i:
            if j != "c":
                new+=i
    print( new) 
    print( my_string)
