# -*- coding: utf-8 -*-
"""
Solução do exercício 3, aula 10: Harshad

@author: Fabio
"""

def is_harshad(numero):
    # Caso o numero seja zero, não há a necessidade de continuar esta função,
    # basta retornar False.
    if numero == 0:
        return False

    # Se chegamos até aqui, é porque o número não é nulo. Logo, temos que 
    # verificar realmente se o número é Harshad.
        
    # Copia o número original para não perder o seu valor.
    n = numero
    
    # Calcula a soma dos dígitos do número que foi passado para a função.
    soma_digitos = 0
    while n > 0:
        digito = n % 10
        soma_digitos += digito
        n = n // 10
    
    # Verifica se o número original é Harshad.
    if numero % soma_digitos == 0:
        return True
    else:
        return False
