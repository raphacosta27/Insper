lista = []
for i in range(10):
    valor = int(input("digite um valor: "))
    lista.append(valor)
maior = lista[0]
indice_do_maior = 0
for i in range(1,10):
    if maior < lista[i]:
       maior = lista[i]
       indice_do_maior = i           # equivalente a maior = max(lista)
print ('o maior numero é: ', maior)
print ('ele esta na posição {0} da lista'.format(indice_do_maior))
    
    