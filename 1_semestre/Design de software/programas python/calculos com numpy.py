import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
#linspace faz com que ele gere numeros que estão entre 0 e 2pi, gerando 100 números
y = np.sin(x)

plt.plot(x, y)
plt.show()