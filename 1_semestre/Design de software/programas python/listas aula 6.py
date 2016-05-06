import math
import matplotlib.pyplot as plt

angle = 0
lista_seno=[]
lista_cossenos=[]

while angle <= math.pi*2 :
     lista_seno.append(math.sin(angle))
     lista_cossenos.append(math.cos(angle))
     angle += 0.1

plt.plot(lista_seno, lista_cossenos)
plt.show()

