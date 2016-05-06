import math
frangos = 1000
meses = 0
while frangos > 0:
    frangos = math.floor(frangos * 1.12) 
    frangos -= 150
    meses +=1
print ("Passaram-se {0} meses".format(meses))