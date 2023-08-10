# Write a program to input a string and print if it is palindrome or not.
s=input(" enter string : ")
def peli(s):
    s1=s[::-1]
    if s==s1:
        print("given string is pelindrome")
    else:
        print("given string is not pelindrom")
peli(s)
