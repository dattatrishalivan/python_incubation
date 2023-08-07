#  Print Elements at Odd indexes from a list (Using for loop)
# l = [10,11,20, 21,30, 31, 40, 41]
l = [10,11,20, 21,30, 31, 40, 41]
def odd(l):
    for i in range(1,len(l),2):
        print(l[i])
odd(l)