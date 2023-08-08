"""WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the
BMI.
Write code that calls this function after taking height and weight as inputs and then prints
underweight, normal, overweight or obese depending on the value of BMI."""
def bmi(height,weight):
    bmi=weight/((height/100)**2)
    if bmi<=18.5:
        print("underweight")
    elif bmi>18.5 and bmi<=24.9:
        print("healthy")
    elif bmi>24.9 and bmi<=29.9:
        print("overweight")
    else:
        print("obsessed")
height=float(input("enter height in cm : "))
weight=float(input("enter weight : "))
bmi(height,weight)