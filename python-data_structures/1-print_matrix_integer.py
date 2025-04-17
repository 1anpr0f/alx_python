def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            i.append(int(j))
        print("{:d}".format(i))
                  
