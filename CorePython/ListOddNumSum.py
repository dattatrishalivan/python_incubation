# Write a function that takes a list of numbers from user as argument and returns the sum of only
# odd numbers (Use only for loop. No need to use if statement).
l=1
h=10
def odd_sum(l,h):
    sum=0
    for i in range(l,h,2):
       sum=sum+i
    print("sum of odd numbers : ", sum)
odd_sum(l,h)