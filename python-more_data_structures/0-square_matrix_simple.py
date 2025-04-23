def square_matrix_simple(matrix=[]):
    for i in matrix:
        for  j in i:
          itr = "{:d}".format(j)
          i = ", ".join(itr)
        print(list(map(lambda x:x**2,i)))
        

  