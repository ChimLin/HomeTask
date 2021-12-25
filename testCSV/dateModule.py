import datetime

d = datetime.datetime(2021, 12, 24)

print(d.year)
print(d.month)
print(d.day)

date = datetime.datetime.now()
print(date)
date1 = datetime.datetime.today()
print(date1)

today = datetime.datetime.today()
print(today.strftime("%d/%m/%y"))

now = datetime.datetime.now()
last = datetime.datetime(2020, 3, 20)

difference = now - last

print(difference.days)
print(difference.seconds)