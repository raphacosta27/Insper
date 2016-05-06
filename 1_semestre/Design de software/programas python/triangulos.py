#ler a0, n e r 
#termo = a0
#soma = a0
# i = 0
# while i < 0
#    soma+= termo
#    termo += r 
#    i +=1
# print(soma)
a0 = float(input("digite o valor de a0: "))
n = float(input("numero de termos: "))
r = float(input("razao: "))
termo = a0
soma = 0
i = 0
while i < n:
    termo += r 
    i += 1
    print (termo)
    soma +=termo
print ('soma:',soma)




    