def square_matrix_simple(matrix=[]):
    for i in matrix:
        for  k,j in i:
            print("{:d}".format(j**2), end=", " if k < len(i)-1 else end="")
        print()

            