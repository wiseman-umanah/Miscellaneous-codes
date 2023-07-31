from datetime import datetime

def main():
    now = datetime.now()

    #date formatting
    print(now.strftime("The current year is %Y"))
    #%Y/y - year, %A,a - weekday , %b/B - month, %d/D - day of month 
    print(now.strftime("%A, %D %B, %y"))
    
    #%c - locale date and time %x - locale date %X - locale time
    print(now. strftime ("Locale date and time: %c"))
    print(now. strftime ("Locale date: %x"))
    print(now. strftime ("Locale time: %X"))

    #time formatting 
    #%I/%H - 12/24 hrs time, M - minute, %S - second, %p - locale,s AM/PM
    print(now.strftime("current time: %I:%M:%S %p"))
    print(now.strftime("24 hour time: %H:%M"))








main()
