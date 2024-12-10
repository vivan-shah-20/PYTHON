#negative indices can be converted into positive and solved in the same manner

name = "harry"

#both the following will give the same output
print(name[-4:-1])
print(name[1:4])

print(name[:4])
print(name[0:4])

print(name[1:])
print(name[1:5])

#there is also slicing with skip valuesn first 2 indicate the range last digit indicates
#the no to skip counting from the inclusive number
name = "abcdefghijklmnopqrstuvwxyz"
print(name[1:14:3])
