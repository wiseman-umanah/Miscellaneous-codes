'''from datetime import datetime

twentyfour = [" ",13,14,15,16,17,18,19,20,21,22,23,0]
hour = int(input("input number of the 12 hours: "))
minutes = int(input("input number of the minutes: "))
print("What is the time division")
meridian = ('AM','PM')
for i,d in enumerate(meridian):
   print(i,":",d)
meri = int(input())
your_time = str(hour)+":"+str(minutes)+" "+meridian[meri]
print("Your time is",str(your_time))

if meri == 1:
   hour = twentyfour[hour]
   your_time = str(hour)+":"+str(minutes)
   print("In military,the time is",str(your_time))
else:
   your_time = str(hour)+":"+str(minutes)
   print("In military,the time is",str(your_time))
   


print("type your time in 12hour format- 09:23 PM")
print("Time format- hour:minutes AM/PM")
twentyfour= {"1":"13","2":"14", "3": "15", "4": "16", "5": "17", "6": "18", "7": "19", "8":"20","9": "21", "10": "22", "11": "23", "12": "0"}
time = input()
time = time.upper()
time=time.split(" ")
if "PM" in time:
   t1=time[0].split(":")
   minute=t1[1]
   hour=twentyfour[t1[0]]
   print(hour +":"+ minute)
else:
   print(time[0])
'''
import datetime
time = input()
formatTime = datetime.datetime.strptime(time,'%I:%M %p')
newTime = formatTime.strftime('%H:%M')

