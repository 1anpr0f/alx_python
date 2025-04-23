def square_matrix_simple(matrix=[]):
    for i in matrix:
        for  j in i:
            print("{:d}".format(j), end=", " if j != i[-1] else "")
        print(map(lambda x:x**2,i))
        print()

  