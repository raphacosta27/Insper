# -*- coding: utf-8 -*-
"""
Solução exercício 2a.
"""

import numpy as np

def maior_diagonal(A):
    num_linhas = A.shape[0]
    maior = A[0][0]
    for i in range(num_linhas):
        if A[i][i] > maior:
            maior = A[i][i]
    return maior

# Codigo de teste
A = np.array([[1, 2, 3], [7, 7, 7], [-3, 9, -4]])
print(maior_diagonal(A))
