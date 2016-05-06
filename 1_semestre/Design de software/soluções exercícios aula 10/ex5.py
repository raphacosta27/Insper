# -*- coding: utf-8 -*-
"""
Solução do exercício 5, aula 10: contar palavras.

@author: Fabio
"""

def conta_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem
