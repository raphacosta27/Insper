from random import randint

n = 10000
soma = 0 
contador = 0 

while contador < n:
    valor = randint(1,100)
    soma += valor 
    contador += 1 
print(soma/n)    