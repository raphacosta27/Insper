soma = 0
while True:
    valor = float(input("Digite um valor "))
    if valor < 0:
        break
    else:
        soma += valor
print("A soma é {0}".format(soma))        