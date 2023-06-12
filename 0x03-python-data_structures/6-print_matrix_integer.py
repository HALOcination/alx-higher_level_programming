#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        print(' '.join('{:d}'.format(m)for m in n))
