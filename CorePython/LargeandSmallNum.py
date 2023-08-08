# Take input of age of 3 people by user and determine oldest and youngest among them.
a=int(input("enter age of person1 :"))
b=int(input("enter age of person2 :"))
c=int(input("enter age of person3 :"))
if a>b and a>c:
    print("person1 is oldest")
elif b>a and b>c:
    print("person2 is oldest")
else:
    print("person3 is oldest")
if a < b and a < c:
    print("person1 is younger")
elif b < a and b < c:
    print("person2 is younger")
else:
   print("person3 is younger")
