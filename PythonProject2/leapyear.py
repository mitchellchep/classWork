"""A year is a leap year if:

1)It is divisible by 4, and

2)It is not divisible by 100, unless

3)It is also divisible by 400.

"""

def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            #If it is also divisible by 100, it is NOT a leap year,
            #Unless it is also divisible by 400, then it IS a leap year.
            leap = True

    return leap



year = int(input("Enter a year: "))
print(is_leap(year))