n = int(input("Digite um numero inteiro positivo "))
tem_divisor = False
d = 2
while d < n:
    if n % d == 0:
        tem_divisor = True
        break
    d = d + 1 
if tem_divisor:
    print ("o numero {0} é composto".format(n))
else:
    print("o numero {0} é composto".format(n))