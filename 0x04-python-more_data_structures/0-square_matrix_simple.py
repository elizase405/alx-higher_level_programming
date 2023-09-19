#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst1 = []
    matrix_lst = []

    for i in matrix:
        for j in i:
            lst1.append(j*j)
        matrix_lst.append(lst1)
        lst1 = []

    return matrix_lst
