# -*- coding: utf-8 -*-
"""
Solução exercício 2b.
"""

import numpy as np

def transposta(A):
    num_linhas = A.shape[0]
    num_colunas = A.shape[1]

    B = np.zeros([num_colunas, num_linhas])

    for i in range(num_linhas):
        for j in range(num_colunas):
            B[j][i] = A[i][j]
    return B

# Codigo de teste
A = np.array([[1, 2, 3], [7, 7, 7], [-3, 9, -4]])
print(A)
print()
print(transposta(A))
