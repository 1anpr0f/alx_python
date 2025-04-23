def square_matrix_simple(matrix=[]):
    for i in matrix:
        for  j in i:
            add_new = "{:d}".format(j**2),end=", " if j !=i[-1] else ""
            i = add_new
        print(i,end="")
    

  