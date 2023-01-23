#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            end = "" if matrix[i][-1] == matrix[i][j] else " "
            print("{:d}".format(matrix[i][j]), end=end)
        print()
