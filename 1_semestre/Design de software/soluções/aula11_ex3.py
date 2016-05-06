# -*- coding: utf-8 -*-
"""
Solução exercício 3.
"""

import random
import math

lista = []
for i in range(10):
    lista.append(random.uniform(1, 10))

contagem = {}
for elemento in lista:
    chave = math.floor(elemento)
    if chave in contagem:
        contagem[chave] += 1
    else:
        contagem[chave] = 1

print(lista)
print(contagem)
