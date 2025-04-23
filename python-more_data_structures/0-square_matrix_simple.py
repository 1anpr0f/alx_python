def square_matrix_simple(matrix=[]):
    for new_row in matrix:
        new_row = [x**2 for x in new_row]
        matrix.append(new_row)
    return matrix
    

  