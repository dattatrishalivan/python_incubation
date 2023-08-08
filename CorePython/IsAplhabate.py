"""WAF: is_alphabet() that takes a string argument and returns True or False. True if all characters
in the string are alphabets otherwise False. (write code using for loop and if. Do not use built-in
functions)"""
s=input("enter string : ")
alp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def is_alphabet(s):
    for i in s:
        if i not in alp:
            return False
    else:
        return True
print(is_alphabet(s))


