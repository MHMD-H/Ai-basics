import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("-" * 40)
# Print The Current  Time
print(datetime.datetime.now().time())
print("-" * 40)

print(datetime.datetime.now().year) #year(2025)
print(datetime.datetime.now().month) #month(8)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)

print("-" * 40)
print(datetime.datetime.min)
print(datetime.datetime.max)
print("-" * 40)

#print specific date ---> datetime.datetime(year,month,day,hour,minute,second,femto second)
print(datetime.datetime(2006,7,17,6,50,30,87995))
#__________________________________________________________________________________________________________________

#formatting to date time
my_birthday_day = datetime.datetime(2009,2,3).strftime("%A")
print(my_birthday_day)
my_birthday_month = datetime.datetime(2006,7,17).strftime("%B")
print(my_birthday_month)

my_birthday_ = datetime.datetime(2006,7,17,6,30,50).strftime("%p")
print(my_birthday_)

#________________________________________________________________________________________________________________________________
# +- time
from datetime import timedelta 
from datetime import datetime
tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow) 

timer = timedelta(seconds=10)
