"""WAF: mean() that returns the mean of list of numbers passed to the function"""
l=[22,44,23,65,78,11,98,78,66]
def mean(l):
    avg=0
    mean=0
    l1=len(l)
    #print(l1)
    for i in l:
        mean+=i
    avg=mean/l1
    print("mean of given list numbers is : ",round(avg,2))
mean(l)
