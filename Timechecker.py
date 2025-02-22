# This script displays either good morning or good evening when it checks the system time.

#import datetime library
import datetime

#morning period
start = datetime.time(0, 0, 0)
end = datetime.time(11, 59, 59)

#evening period
start2 = datetime.time (16, 0, 0)
end2 = datetime.time(23, 59, 59)

#checking current system time
current = datetime.datetime.now().time()


if current <= end:
    print ("Good morning")

elif start2 <= current <= end2:
    print("Good evening")

else:
    print("N/A")










