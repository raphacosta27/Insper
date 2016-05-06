def eh_vogal(a):
       letra = a[0]
       if letra in "aeiouAEIOU":
           return True
       else:
           return False
       
frase = eh_vogal("lo")   
print(frase)     