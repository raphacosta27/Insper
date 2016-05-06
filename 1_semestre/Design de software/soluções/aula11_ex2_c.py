# -*- coding: utf-8 -*-
"""
Solução exercício 2c.
"""
import numpy as np

def is_triangular(A):
    num_linhas = A.shape[0]
    
    for i in range(num_linhas):
        for j in range(i):
            if A[i][j] != 0:
                return False

    return True

# Codigo de teste.
A = np.array([[1, 2, 3], [7, 7, 7], [-3, 9, -4]])
print(is_triangular(A))

B = np.array([[1, 2, 3], [0, 7, 7], [0, 0, -4]])
print(is_triangular(B))
