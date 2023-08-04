"""WAF: count_even_odd() that counts and returns how many numbers are even and how
many are odd in a list of numbers passed as argument."""

l=[1,2,3,4,5,6,7,8,9]
def count_even_odd(l):
    odd,even=0,0
    for i in l:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print("total even number count is : ",even)
    print("total odd number count is : ",odd)
count_even_odd(l)