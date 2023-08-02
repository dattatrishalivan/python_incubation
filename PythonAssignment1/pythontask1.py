import math
""" 1. Predict Output,
S1 = "Hello"
S2 = "This is Python"
print(len(S1), len(S2)) """
def strlen():
    s1 = "Hello"
    s2 = "This is Python"
    print("length of strings s1 and s2")
    print(len(s1), len(s2))  # 5 14
strlen()


"""2. WAP to input a string and print its length."""
def strinput():
    s1=input("enter string to count length : ")  # epam systems
    print("entered string length is : ", len(s1))  # 12
strinput()


"""3. WAP to input 2 numbers and print their sum and difference."""
def adddiff():
    a = eval(input("enter value1 : "))  # 98
    b = eval(input("enter value2 : "))  # 52
    add = a+b
    diff = a-b
    print("addition of 2 num is : ", add)  # 150
    print("diff of 2 num is : ", diff)  # 46
adddiff()


"""4. Predict Output,
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)"""
def strconcat():
    s1 = 'ab'
    s2 = 'de'
    s3 = s1 + s2
    print("concatenation of s1 and s2 is : ", s3)  # abde
strconcat()


"""5. Predict Output,
s1 = 'ab' *4
print(s1)"""
def strmul():
    s1 = 'ab' * 4
    print("multiplication of 'ab' * 4 is : ", s1)  # abababab
strmul()


"""6. WAP to input a string s and a number n. Print the string n times on the screen, 
   each should appear in a separate line (do not use any kind of loops, use the multiplication operator)."""
def strmul_n_times():
    s = input("enter string : ")  # epam
    n = eval(input("enter number : "))  # 5
    print('\n'.join([s]*n))  # print epam n num of times on n number of line
strmul_n_times()


"""7. Predict Output,
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3)
print(len(s3)"""
def strtype():
    s1 = 'Hello'
    s2 = 'This is India'
    s3 = s1 + '\n' + s2
    print(type(s3))  # <class 'str'>
    print(s3)  # Hello This is India
strtype()


"""8. Find the name of function to find the square root. (see all the options available in dir() of builtins)"""
def sqroot():
    print(math.sqrt(25))  # 5.0
    print(math.isqrt(45))  # 6
sqroot()


"""9. WAP to input a number and print its square root ()."""
def sqrootip():
    n = eval(input("enter number : "))  # 78
    print(math.sqrt(n))  # 8.831760866327848
sqrootip()


"""10. WAP to input 4 numbers from user and print their average"""
def numavg():
    n1 = eval(input("enter number1 : "))
    n2 = eval(input("enter number1 : "))
    n3 = eval(input("enter number1 : "))
    n4 = eval(input("enter number1 : "))
    avg = (n1+n2+n3+n4)/4
    print("average of 4 numbers : ", avg)
numavg()


"""11. Use the help function to check what the abs function in python does"""
def helpabs():
    help(abs)  # Return the absolute value of the argument.
    print(abs(-5.90))  # 5.9
    print(abs(-90))  # 90
helpabs()


"""12. What is the output of this code when run from python interpreter.
print(__name__)"""
def fun1():
    print(__name__)  # __main__
fun1()
