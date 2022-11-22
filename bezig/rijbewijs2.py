from datetime import date, datetime


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

A = date(year, month, day)

B = datetime.datetime.now()

print(A)
print(B)

