from datetime import date


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

A = date(year, month, day)
B = date.today()
C = A - B
D = C.days
if D > -6575:
    print("je mag niet rijden")
if D < -6575:
    print("je mag rijden")
