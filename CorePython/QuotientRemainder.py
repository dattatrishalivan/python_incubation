"""WAP get_q_r() taking 2 numbers as parameters and returns the quotient and
remainder in the form of a tuple."""
def get_q_r(n1,n2):
    result=divmod(n1,n2)
    print('Quotient and Remainder = ',result)
n1=int(input("enter num1 : "))
n2=int(input("enter num2 : "))
get_q_r(n1,n2)
