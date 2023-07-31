from cgi import  print_arguments
from datetime import date
from datetime import time 
from datetime import datetime 
from datetime import timedelta

#construct basic timedelta
print(timedelta(hours=5,minutes=1))


# now = datetime.now()
# print('today is',now)
# print('one year from now it will be', str (now + timedelta(days=365)))

# print('in two weeeks and 3 days it will be', str(now + timedelta(days=3,weeks=2)))

# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime ('%A %B %d, %Y')
# print('one week ago it was', s)

# #days until april fool's day
# today = date.today()
# afd = date(today.year,4,1)

# if afd < today:
#     print ( 'april fools day passed', ((today - afd).days), 'days ago')
#     afd = afd.replace(year = today.year + 1)
#     time_to_afd = afd - today
#     print('it is',time_to_afd.days,'days until next april fools day')
