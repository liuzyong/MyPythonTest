# print('Hello World!')
import numpy as np 
from numpy import pi


a = np.array([[1,2,3],[4,5,6]])

# xingzhuang
print(a.shape)

# weidu
print(a.ndim)

# 全零数组
b = np.zeros((2,3))
print(b)

# 全1数组
c = np.ones((2,3), dtype = np.int16)
print(c)

d = np.arange(1,20, 4)
print(d)

# lin = np.linspace(0, 2*pi, 100)
# f = np.sin(lin)
# print(f)

print('random ')
A = np.array( [[1,2],
             [0,14]] )

B = np.array( [[2,0],
           [3,4]] )
print(A*B)
print(A@B)
print(A.dot(B))

print(np.sum(A ,axis =1))
print(np.min(A))
print(np.max(A))