"""WAP to input number of seconds and print in days, hours, minutes and seconds
ex: input = 10000"""
n=int(input("enter total sec : "))
def sec_to_day_convert(n):
    day=int(n/86400)
    tot=n-(86400*day)
    hour=int(tot/3600)
    tot1=tot-(3600*hour)
    min1=int(tot1/60)
    sec1=tot1-(60*min1)
    print(day)
    print(hour)
    print(min1)
    print(sec1)
sec_to_day_convert(n)