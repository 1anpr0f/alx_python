def square_matrix_simple(matrix=[]):
    for i in matrix:
        new_row = [x**2 for x in i]
        matrix.append(new_row)
        return new_row
    

  