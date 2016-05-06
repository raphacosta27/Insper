# -*- coding: utf-8 -*-
"""
Solução do exercício 2, aula 10: intercalar elementos

@author: Fabio
"""

def intercala(lista_1, lista_2):
    lista_nova = []
    for i in range(len(lista_1)):
        lista_nova.append(lista_1[i])
        lista_nova.append(lista_2[i])
    return lista_nova
