#SHAPE
import numpy as np
a = np.array([[1,2,3],[1,2,4]])
print(a)
print() #gives a blank space
print(a.shape)
print()

#RESHAPE
a = np.array([1,2,3,4])
b = a.reshape(2,2)        # from 1 dimensional it has become 2 dimensional
print(a,a.ndim)
print()
print(b,b.ndim)
print()


c = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d = c.reshape(2,3,2)        # from 1 dimensional it has become 3 dimensional
print(c,c.ndim)
print()
print(d,d.ndim)

one = d.reshape(-1)         # from 3 dimensional we made it into 1 dimensional
print(one)
