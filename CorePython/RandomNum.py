# Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use
# a for loop.
import random
def random_num():
    sum=0
    l=[]
    for i in range(0,5):
        num=random.randrange(1,1000)
        l.append(num)
        sum=sum+num
    avg=sum/5
    print("random number lis : ",l)
    print("Sum os 5 random number : ", sum)
    print("Average of random numbers : ", avg)
random_num()