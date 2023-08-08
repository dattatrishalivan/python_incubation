"""WAF get_si() that takes Principle, Rate and Time as arguments and returns the Simple
Interest."""
def fun_si(p,t,r):
    si=(p*t*r)/100
    print("simple interest : ", si)
p=int(input("enter principle : "))
t=int(input("enter time : "))
r=int(input("enter rate of interest : "))
fun_si(p,t,r)
