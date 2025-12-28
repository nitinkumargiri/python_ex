# take a input from user and create a calendar of month.
import calendar
year = int (input ("nteer your year: "))
month = int (input("enter your month: "))
cal = calendar.monthcalendar(year,month)
for week in cal:
    for day in week:
        if day == 0:
            print ("  ",end=" ")
        else:
            print(f"{day:2}",end=" ")
            print()