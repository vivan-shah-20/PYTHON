#RANDOM

#Rand() [gives positive numbers only]
import numpy as np
a = np.random.rand(4)       #1 dimensional
print (a)

b = np.random.rand(3,4)     #2 dimensional
print (b)


#Randn()  [gives positive as well as negative numbers]
c = np.random.randn(4)      #1 dimensional
print(c)


#Ranf()
d = np.random.ranf(4)   #gives random values between 0 to 1, does not include 1
print(d)


#Randint()
e = np.random.randint(1,20,7)   # e = np.ramdom.randint(min valus,max value,total values)
print(e)
