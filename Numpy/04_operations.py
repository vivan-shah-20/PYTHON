#zeroes
import numpy as np
a = np.zeros(4)     # 4 indicates number of input in the array
b = np.zeros((3,4)) # this creates a 2 dimensional array
print(a)
print()
print(b)
print()


# ones
c = np.ones((3,4))
print(c)
print()

#empty array
d = np.empty((3,4))  #whenever an empty array is created it takees the value of previous input
print(d)
print()

#arange elements
e = np.arange(4)
print(e)
print()

#diagonal elements as 1
f = np.eye(3,4)
print(f)
print()

#linspace
g = np.linspace(0,10,5)   #divides the space from 0 to 10 in 5 equal parts
print(g)
