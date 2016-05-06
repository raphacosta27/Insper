total = 0
while True:
    codigo = int(input("digite o codigo do produto "))
    if codigo == 0:
        break
    elif codigo == 1:
        valor_unitario = 0.5
    elif codigo == 2:
        valor_unitario = 1.0
    elif codigo == 3:
        valor_unitario = 4.0
    elif codigo == 5:
        valor_unitario = 7.0
    elif codigo == 9:
        valor_unitario = 8.0
    else:
        print("codigo invalido")
        continue
    
    quantidade = float(input("quantos produtos voce comprou deste tipo? "))
    total += valor_unitario * quantidade
print("o valor total é {0}".format(total))    
    
    