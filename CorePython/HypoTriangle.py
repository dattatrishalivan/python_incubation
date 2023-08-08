"""WAP to find the length of hypotenuse of a rightangled triangle, input the height and
base from user."""
from math import sqrt
def hype_triangle(height, base):
   h = sqrt(height*height + base*base)
   return h
n1=int(input("enter height : "))
n2=int(input("enter base : "))
print(hype_triangle(n1,n2))