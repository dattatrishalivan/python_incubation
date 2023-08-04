"""WAF: maximum() to return the largest number in a list of numbers (do not use max
function). Function takes a list or tuple of numbers as argument."""

l=[22,44,23,65,78,11,98,78,66]
def maximum(l):
    max_num=0
    for i in l:
        if max_num<i:
            max_num=i
    print("Max number is : ",max_num)
maximum(l)
