#JOIN ARRAY
import numpy as np
a = np.array([1,2,3,4])
b = np.array([9,8,7,6])

c = np.concatenate((a,b))  #both the array join together
print(c)
print()

d = np.array([[1,2,3,4],[6,7,8,9]])
e = np.array([[9,8,7,6],[1,2,3,4]])

f = np.concatenate((d,e), axis = 1) 
g = np.concatenate((d,e), axis = 0)  
h = np.dstack((d,e))          # HEIGHT
i = np.hstack((d,e))          # ROW
j = np.vstack((d,e))          # COLUMN
print(f)
print()
print(g)
print()
print(h)
print()
print(i)
print()
print(j)
