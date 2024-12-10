# normal numpy array
'''import numpy as np
a = np.array([0,9,8])
print(a)
print(type(a))'''


#converting list into array
import numpy as np
l = []

for i in range(1,5):                            # for number of inputs you want to take 
    a = int(input("enter the number:"))
    l.append(a)
    
print(np.array(l))