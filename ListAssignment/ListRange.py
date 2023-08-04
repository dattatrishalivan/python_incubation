"""WAF: find_in_range() that takes a three arguments:
a list of numbers, start, end
The function returns a list of numbers from the original list, which lie between start and
end.
Ex: find_in_range([3,10, 5, 8, 2, 7], 5, 9)
List of numbers = [3,10, 5, 8, 2, 7]
start = 5
end = 9
list returned should be [5, 8, 7]"""

def find_in_range(l,start,end):
    l1=[]
    for i in l:
        if i>=start and i<=end:
            l1.append(i)
    print(l1)

l=[3,10, 5, 8, 2, 7,3,7,10,4]
start=5
end=9
find_in_range(l,start,end)