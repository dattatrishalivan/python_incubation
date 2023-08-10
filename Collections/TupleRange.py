"""Use the range method and create a tuple containing the following values:
	(20, 15, 10, 5)"""

l=[]
for i in range(20,1,-5):
    l.append(i)
t=tuple(l)
print(t)
