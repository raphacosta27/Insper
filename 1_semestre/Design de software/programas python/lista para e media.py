lista = []
while True:
    valor = float(input("digite um valor: "))
    if valor < 0:
        break
    lista.append(valor)
if len(lista) == 0:
    print("lista vazia, nao posso calcular média")
else:
    soma = 0 
    for elemento in lista:
        soma += elemento
        print("media: {0}".format(soma/len(lista)))       