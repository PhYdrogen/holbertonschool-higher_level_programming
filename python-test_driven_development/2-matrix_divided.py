#!/usr/bin/python3
""" Doc
"""


def matrix_divided(matrix, div):
    """ Doc
    """
    if (type(div) is not int) and (type(div) is not float):
        raise TypeError('div must be a number')
    if matrix is None or type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    len_matrix = len(matrix)
    new_matrix = []
    for list_row in matrix:
        new_row_matrix = []
        for elem in list_row:
            try:
                rep = elem / div
                new_row_matrix.append(round(rep, 2))
            except ZeroDivisionError:
                raise ZeroDivisionError('division by zero')
        new_matrix.append(new_row_matrix)

    return new_matrix
