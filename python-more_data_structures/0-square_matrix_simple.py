#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def sqrt(x):
        return x**x
    new_matrix = []
    for i in matrix:
        for j in matrix[i]:
            new_matrix[i][j] = sqrt(i)
    return nex_matrix
