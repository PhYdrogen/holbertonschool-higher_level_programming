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
    if type(matrix[0]) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if div == float('inf') or div == -float('inf') or div != div:
        div = 1000

    len_matrix = len(matrix[0])
    new_matrix = []
    for list_row in matrix:
        new_row_matrix = []
        if len_matrix != len(list_row):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in list_row:
            try:
                rep = elem / div
                new_row_matrix.append(round(rep, 2))
            except ZeroDivisionError:
                raise ZeroDivisionError('division by zero')
            except TypeError:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        new_matrix.append(new_row_matrix)

    return new_matrix
