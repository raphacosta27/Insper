# -*- coding: utf-8 -*-
"""
Solução aula 11, exercício 4.
"""

# Eis o código original:
lista = [4, 2, 1, 3]
n = len(lista)

for i in range(n - 1):
    j = i + 1
    while j <= n - 1:
        if lista[i] > lista[j]:
            troca = lista[i]
            lista[i] = lista[j]
            lista[j] = troca
        print("Olá!")
        j += 1

print(lista)
print(i)
print(j)

# Se você rodar esse código, verá a solução imediatamente. O motivo do 
# exercício era praticar o teste de mesa.
#
# Vamos entender esse algoritmo de um ponto de vista de mais alto nível:
# - O laço externo (for i in range(n-1)) avança desde o início da lista até a 
#   penúltima posição.
#
# - O código do if é, em português, o seguinte:
#
#   se o i-ésimo elemento da lista for maior que o j-ésimo elemento:
#       troca esses dois elementos de lugar!
#
# - O laço interno é um 'for' disfarçado! Essa estrutura:
#
#     j = i + 1
#     while j <= n - 1:
#         <troca lista[i] com lista[j] se lista[i] > lista[j]>
#         print("Olá")
#         j += 1
#
#   equivale a:
#
#     for j in range(i + 1, n):
#         <troca lista[i] com lista[j] se lista[i] > lista[j]
#         print("Olá")
#
# - Portanto, para cada posição i da lista, começando de zero, o algoritmo 
#   efetua uma série de trocas de valor com o objetivo de trazer o menor 
#   elemento do segmento lista[(i+1):] para a posição i. Ao terminar, os 
#   elementos da lista terão sido reordenados em ordem crescente!
#
# Temos aqui uma implementação de um algoritmo de ordenação conhecido como 
# "selection sort" (ordenação por seleção). Este algoritmo é simples mas pouco
# eficiente, se comparado com outros algoritmos eficientes de ordenação (como
# quicksort, mergesort, ou heapsort).
