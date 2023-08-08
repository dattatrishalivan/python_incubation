"""WAF: is_leap_year() that takes a year as input and retuns True if year is leap year, otherwise
false."""
year=eval(input("enter year : "))
def is_leap_year(year):
    if year%400==0 and year%100==0:
        print(year," is leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print(year, " is leap year")
    else:
        print(year, " is not leap year")
is_leap_year(year)
