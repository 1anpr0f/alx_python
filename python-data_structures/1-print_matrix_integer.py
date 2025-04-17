def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if i.count(j) == 3:
                return
            print("{:d}".format(j),end="")
    return matrix
          
