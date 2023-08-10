"""WAP to join a list and a tuple:
L = [1,3,5,7]
T = (8,6,4,2)
Store the result in a list LS"""
L = [1,3,5,7]
T = (8,6,4,2)
LS=L
for i in T:
    LS.append(i)
print(LS)

#Print Elements at Odd indexes from a list (Do not use loop)
l = [10,11,20, 21,30, 31, 40, 41]
print(l[1::2])

