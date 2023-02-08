#!/usr/bin/python3
""" Doc
"""


def pascal_triangle(n):
    """ Doc
    """
    if not isinstance(n, int):
        return []
    if n <= 0:
        return []

    matrix = []
    for n in range(n):
        matrix_row = []
        if n == 0:
            matrix_row.append(1)
        elif n == 1:
            matrix_row.append(1)
            matrix_row.append(1)
        else:
            for x in range(n-1):
                matrix_row.append(matrix[n-1][x] + matrix[n-1][x+1])
            matrix_row.append(1)
            matrix_row.insert(0, 1)
        matrix.append(matrix_row)
    return matrix
