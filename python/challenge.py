import calendar


def countdays (year,month,day):
    daycount = 0
    weekslist = calendar.monthcalendar(year,month)
    for week in weekslist:
        if week[day] != 0:
            daycount += 1
    return daycount

run = True
while(run):
    try:
        print('Which day of the week do you want to count?')
        x =list(calendar.day_name)
        for i,d in enumerate(x):
            print(i, ':',d)
        print("Or type 'exit to end")
        
        day = input("? ")
        if day == 'exit':
            run = False
            break
        day = int(day)
        year =int(input("Enter year: "))
        month = int(input("Enter month: "))
         
        result = countdays(year,month,day)
        print("We have",str(result), "of those days in the month and year specified")
    except Exception as e :
        print(e)
        print ("sorry, that's not valid input")
