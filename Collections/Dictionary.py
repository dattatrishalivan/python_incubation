"""WAP to create a dictionary of numbers mapped to their negative value for numbers from 1-5.
The dictionary should contain something like this:
Do with both with and without range based for loop.
{1:-1,2:-2,3:-3….} """
d={}
for i in range(1,5+1):
    for j in range(1,i+1):
        d[i]=-j
print(d)

"""Read help for zip and write a program that has two lists
l1 = [1,2,3,4]
l2 = [10,20,30,40]
And converts them to a dictionary d containing { 1:10,2:20 …….}"""
l1 = [1,2,3,4]
l2 = [10,20,30,40]
d={}
d1=dict(zip(l1,l2))
print(d1)
for i in l1:
    for j in l2:
        d[i]=j
        l2.remove(j)
        break
print(d)


