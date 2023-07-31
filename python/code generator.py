import random,time, sys

def Generator():
   passWord = str(random.randint(0,999999))
   if len(passWord)== 6:
      print(int(passWord),"\nPress enter(CTL+C to quit)",end="")
   else:
      Generator()

try:
   Generator()
   while True:
      for i in range(1):
         n = input()
         if n == "":
            time.sleep(1)
            Generator()
         else:
            print("wrong input")

except KeyboardInterrupt:
   print("Ended")
   sys.exit()

#code generator that generator randomly once enter is clicked within 2 seconds of time 
