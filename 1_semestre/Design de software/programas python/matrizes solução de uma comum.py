import numpy as np

#x + 2y + z = 8
#2x - y + z = 3 
#3x + y - z = 2
a = np.array([[1, 2, 1], [2, -1, 1], [3, 1, -1]])
b = np.array([8, 3, 2])
z = np.linalg.solve(a,b)
print(z) 