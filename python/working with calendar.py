import calendar

c = calendar.TextCalendar(calendar.MONDAY)
# str = c. formatmonth(2022,1,0,0)
# print(str)

# using html
# hc= calendar.HTMLCalendar(calendar.SUNDAY)
# str = hc.formatmonth(2022,1)
# print(str)

#looping over days of a month
#zero means that the day of the week is in an overlapping month
# for i in c.itermonthdays(2022,8):
#     print(i)


#getting the calendar month and days from locale
for name in calendar.month_name:
    print(name)


# for d in calendar.day_name:
#     print(d)

# #TODO : Calculate days based on a rule
# # a team meeting on first friday of every month.
# # to figure out what days that would be for each month 
# # we can use this script

# print('team meetings will be on:')
# for m in range(1,13):
#     cal = calendar.monthcalendar(2022,m)
#     weekone = cal[0]
#     weektwo = cal[1]
#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]

#     print(calendar.month_name[m],meetday)