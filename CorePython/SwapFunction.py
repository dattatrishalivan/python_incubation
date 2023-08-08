#WAP to input 2 strings and swap the strings
def swap():
    a=input("entar string1 : ")
    b=input("enter string2 : ")
    print("string1 before swap :",a)
    print("string2 before swap: ",b)
    a,b=b,a
    print("String1 after swap : ",a)
    print("String2 after swap : ",b)
swap()
