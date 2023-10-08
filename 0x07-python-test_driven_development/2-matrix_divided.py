#!/usr/bin/python3

"""
matrix_divided module contains 1 function: matrix_divided

>>> matrix_divided([[2,4],[6,8]], 2)
[[1,2],[3,4]]

"""


def matrix_divided(matrix, div):
    """
    matrix_divided is a function that divides all elements of a matrix
    Only integer and float values are allowed

    raises:
    TypeError: if div is not an integer or float
    TypeError: if rows are not of same length
    TypeError: if rows are not of made up of ints and floats.
    ZeroDivisionError: if div is 0
    """

    ls = []

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        lsr = []
        if ((len(i) != len(matrix[0]))):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            else:
                lsr.append(round(j/div, 2))
        ls.append(lsr)

    return ls
