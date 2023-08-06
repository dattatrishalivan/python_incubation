"""create Student class,
add constructor with 2 arguments for name and age, to set the name and age attributes.
Create a student object,initialize it with some values and print its attributes."""
class Student:
    def __init__(self,name, age):
        self.name=name
        self.age=age
s=Student('datta',33)
print(s.name)
print(s.age)