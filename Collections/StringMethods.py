#WAP to input a string and remove all spaces from it.
s="epam systems limited"
s1=s.replace(" ","")
print(s1)

#WAP to print all methods(functions/operations) available in a string (Hint : dir())
print(dir(str))

"""Write statement to check if rstrip method is available in the str class.
(Hint : Use the find function or in)"""

if "lstrip" in dir(str):
    print(True)
else:
    print(False)

#WAP to input a string and replace all space with new lines (\n) and print again.
s="epam systems limited"
s1=s.replace(" ","\n")
print(s1)