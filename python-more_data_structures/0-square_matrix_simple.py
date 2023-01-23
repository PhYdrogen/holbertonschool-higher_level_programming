#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix_row = []
        for j in range(len(matrix[0])):
            act = matrix[i][j]
            new_matrix_row.append(act * act)
        new_matrix.append(new_matrix_row)
    return new_matrix
