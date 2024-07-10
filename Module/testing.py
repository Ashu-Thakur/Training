# from Package import mymodule as f, mymodule2 as f2

# f.Greet("Ashutosh")

# f2.Welcome()

# import Package
# import time
# print(Package.__all__)
# print(dir(time))


# !====================Time module========================
import time
import datetime

print(dir(time))
print(time.time())#current time
print(time.daylight)
print(time.asctime())
# print(time.sleep(2)) #for delay

# datetime module
# print(datetime.datetime(2024,7,9))
print(datetime.date.today())
print(datetime.date.today().month,datetime.date.today().year,datetime.date.today().day)
print(datetime.datetime.fromtimestamp(1887639468))
# print(datetime.datetime.isocalendar())
# print(datetime.datetime.isoweekday())

timestamp = datetime.datetime(2024,7,9,18,33)
print(timestamp.timestamp())
print(datetime.datetime.fromtimestamp(timestamp.timestamp()))


# !random module
import random

