"""WAF: second_maximum() Create a new version of above code to return the second-largest
number."""
l=[22,44,23,65,78,11,98,78,66]
def sec_maximum(l):
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    l1.sort()
    print("Sec max number is : ", l1[-2])
sec_maximum(l)

