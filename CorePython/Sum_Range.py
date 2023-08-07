# WAP to input a number and print all numbers from 1 till that number
n=int(input("input number : "))
def num_sum(n):
    for i in range(1,n+1):
        print(i)
num_sum(n)