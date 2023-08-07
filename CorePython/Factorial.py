"""WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number
    whose factorial is to be found.
        Ex: if n = 4 output should be 24
        4! = 1x2x3x4 = 24"""
n=int(input("enter input number : "))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(n)