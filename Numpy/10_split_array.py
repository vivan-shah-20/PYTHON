#SPLIT ARRAY
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
print()

b = np.array_split(a,3)
print(b,type(b))          #this becomes a list
print(b[0])               #to print only first array
