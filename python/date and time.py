from datetime import date
from datetime import time 
from datetime import datetime

def main():
    # today = date.today()
    # print("today's date is",today)

    # print('Date comps: ' , today.day, today. month, today.year)

    # print('todays weekday is', today.weekday())
    # days = ['mon','tue','wed','thur','fri','sat','sun']
    # print("which is a",days[today.weekday()])


     today = datetime.now()
     print("\n",'the current date and time is', today)

    # t = datetime.date( datetime.now())
    # print("\n","the cuurrent date is",t)

    # ti = datetime.time ( datetime.now())
    # print("\n","the cuurrent time is",ti)






main()