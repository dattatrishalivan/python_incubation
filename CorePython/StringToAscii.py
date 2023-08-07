# WAP to input a string and print the ASCII value of each character in the string.
s=input("enter string : ")
def string_to_char_print(s):
    for i in s:
        print("ASCII value of '",i,"' is : ",ord(i))
string_to_char_print(s)