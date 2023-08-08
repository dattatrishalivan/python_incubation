# WAP get_ci() that takes Principle, Rate and Time as arguments and returns the
# Compound Interest.
def fun_ci(p,r,t):
    amount=p*(pow((1+r/100),t))
    ci=amount-p
    print("compound interest : ",ci)
p=int(input("enter principle : "))
r=int(input("enter time : "))
t=int(input("enter rate of interest : "))
fun_ci(p,r,t)