# WAP to input a list of numbers and store in a tuple. Now input another number and print the
# index of this number in the tuple.
def tuple_index():
    t1=[]
    n = int(input("numbers : "))
    for i in range(0,n):
        items=int(input())
        t1.append(items)
    tup=tuple(t1)
    print(tup)
    l1=list(tup)
    n1=int(input("enter no to insert in tuple : "))
    l1.append(n1)
    tup1=tuple(l1)
    print("tuple values : ", tup1)
    val=tup1.index(n1)
    print("index of insesertd number ",val)
tuple_index()


