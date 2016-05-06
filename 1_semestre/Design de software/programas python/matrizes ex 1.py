import numpy as np
def multiplica(a,b):
    produto = np.zeros([2,2])
    produto[0][0] = a[0][0]*b[0][0] + a[0][1]*b[1][0]
    produto[0][1] = a[0][0]*b[0][1] + a[0][1]*b[1][1]
    produto[1][0] = a[1][0]*b[0][0] + a[1][1]*b[1][0]
    produto[1][1] = a[1][0]*b[0][1] + a[1][1]*b[1][1]
    return produto

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(multiplica(x,y))
    
    
    