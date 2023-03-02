#!/usr/bin/python3
""" module that divides a matrix by a number """


def checkType(matrix):
   """ function that checks if the matrix are of the same type """

   for i in matrix:
        for j in i:
            if all(isinstance(n, (int, float)) for n in i) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
def matrix_divided(matrix, div):
    """ function that divides a given matrix by a number """

    i = 0
    j = 0
    
    checkType(matrix)

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if len(set(map(len, matrix)))!=1:
        raise TypeError("Each row of the matrix must have the same size")
    """
    else:
        raise TypeError("Each row of the matrix must have the same size")
"""
    matrix = [[round(x/div, 2) for x in l] for l in matrix]
    return matrix
