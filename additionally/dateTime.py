""" """

import locale

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

d1 = date(2024, 8, 24)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(16, 41, 38)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)

print(date.today())

print(date.max)
print(date.min)
print(time.min)
print(time.max)

dt = datetime(2024, 8, 24, 16, 44, 26)
print(dt)

print(dt.date().year)

now = datetime.now()
print(now)

dt = datetime.strptime("16/10/2002", "%d/%m/%Y")
print(dt)

dt = datetime.strptime("16/10/2002 00:24", "%d/%m/%Y %H:%M")
print(dt)

print(locale.setlocale(locale.LC_ALL, ""))

now = datetime.now()
print(now.strftime("%Y-%m-%d (%a)"))

delta1 = timedelta(days=2, hours=1, minutes=10)
delta2 = timedelta(days=3, hours=2, minutes=5)
print(delta2 - delta1)
