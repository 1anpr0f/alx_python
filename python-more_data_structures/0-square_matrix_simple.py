def square_matrix_simple(matrix=[]):
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=", " else end="")
        sqr =list(map(lambda x:x**2,i))
        print(sqr) 
            