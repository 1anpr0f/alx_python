def square_matrix_simple(matrix=[]):
    for i in matrix:
        for  j in i:
           i.append(j)
           ", ".join(i)
        print(list(map(lambda x:x**2,i)))
        

  