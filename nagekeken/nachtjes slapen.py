from datetime import date


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

A = date(year, month, day)
B = date.today()
C = A - B
print("aantal dagen tot datum", C.days)