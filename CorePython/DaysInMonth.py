"""WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
as arguments and returns the number of days in the month.
Use the function is_leap_year() to check the special case of 29 days in leap year for month of
FEB. [Use dictionary to store the mapping of month and days.]"""

mon = eval(input("enter month : "))
year = eval(input("enter month : "))
dict = {}


def days_in_month(mon, year):
    if mon == 'feb':
        def leap(mon):
            if ((mon == 'feb') and ((year % 4 == 0) or ((year % 400 == 0) and (year % 100 == 0)))):
                dict[mon] = 29
                print(dict)
            else:
                dict[mon] = 28
                print(dict)

        leap(mon)
    elif mon == 'jan' or mon == 'mar' or mon == 'may' or mon == 'jul' or mon == 'aug' or mon == 'oct':
        dict[mon] = 31
        print(dict)
    else:
        dict[mon] = 30
        print(dict)


days_in_month(mon, year)
