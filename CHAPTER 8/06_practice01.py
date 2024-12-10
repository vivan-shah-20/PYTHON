def greatest(a , b , c):
    if (a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("enter a number :"))
b = int(input("enter a number :"))
c = int(input("enter a number :"))
print(greatest(a , b , c))