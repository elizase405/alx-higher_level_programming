#!/usr/bin/python3
def matrix_divided(matrix, div):
    """matrix_divided is a function that divides all elements of a matrix
    Here is a good example
    >>> matrix = [[1,2,3], [4,5,6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix
    [[1,2,3], [4,5,6]]
    
    Here is an example where div is not an integer or float
    >>> matrix = [[1,2,3], [4,5,6]]
    >>> matrix_divided(matrix, "hello")
    div must be a number
    Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
    TypeError: hello
    >>> matrix
    [[1,2,3], [4,5,6]]
    
    Here is an example where div is 0
    >>> matrix = [[1,2,3], [4,5,6]]
    >>> matrix_divided(matrix, 0)
    div must be a number
    Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
    ZeroDivisionError: 0
    >>> matrix
    [[1,2,3], [4,5,6]]
    
    Here is an example where rows are not of same length
    >>> matrix = [[1,2,3,5], [4,5,6]]
    >>> matrix_divided(matrix, 3)
    Each row of the matrix must have the same size
    Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
    TypeError: [[1,2,35], [4,5,6]]
    >>> matrix
    [[1,2,3,5], [4,5,6]]
    
    Here is an example where rows are not of made up of ints and floats.
    >>> matrix = [[1,2,"hi",5], [4,"gffh",6]]
    >>> matrix_divided(matrix, 3)
    matrix must be a matrix (list of lists) of integers/floats
    Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
    TypeError: [[1,2,"hi",5], [4,"gffh",6]]
    >>> matrix
    [[1,2,"hi",5], [4,"gffh",6]]
    """

    ls = []
    ind = 0

    if type(div) != int or type(div) != float:
        print("div must be a number")
        raise TypeError

    if div == 0:
        print("division by zero")
        raise ZeroDivisionError

    for i in matrix:
        lsr = []
        if ((len(i)) != len(matrix[ind++])) & ind != len(matrix) - 1):
            print("Each row of the matrix must have the same size")
            raise TypeError
        for j in i:
            if type(j) != int or type(j) != float:
                print("matrix must be a matrix (list of lists) of integers/floats")
                raise TypeError
            else:
                lsr.append(round(j/div, 2))
        ls.append(lsr)

    return ls

