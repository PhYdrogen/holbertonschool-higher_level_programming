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
        for chffire in range(n):
            matrix_row = []
            if n == 0 or n == 1:
                matrix_row.append(1)
            for o in len(matrix[n-1] - 1):
                res = matrix[n-1][o] + matrix[n-1][o+1]
                matriw_row.append(res)
            matrix_row.insert(0, 1)
            matrix_row.append(1)
        matrix.append(matrix_row)
    return matrix
