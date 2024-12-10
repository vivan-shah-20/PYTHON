import numpy as np
x = np.random.randint(1,100,81).reshape(9,9)
print(x)
l1 = []
for i in range(9):
    sorted = np.sort(x)
    l1.append(max(x[i]))
y = np.array(l1)
print(y)

#TO FIND THE GREATES NUMBER IN EACH ROW AND MAKING A NEW ARRAY