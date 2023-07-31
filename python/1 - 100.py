'''The fibonaccisequence is one of the most famous formulas in mathemathematics
Each number in thesequence is the sum of the two numbers that precedes it
For example: here is the fibonacci sequence for 10 numbers starting from 0; 0,1,1,2,3,5,8,13,21,34

write a program to take N(variable num in code template) positive numbers as input and recursively
calculate and output the first N numbers of the Fibonacci ssequence (starting from 0)
Sample input:
6
Sample output:
0
1
1
2
3
5
!=====If you are making the fibonaccci sequence forn numbers,you shoukd use n<=1
condition as the base case
n = int(input())
def fibonacci(n):
   if n <= 1:
      return n
   else:
      return fibonacci(n-1) + fibonacci(n+2)
for i in range(n,n+1):
   print(fibonacci(i))

#fibonacci(n)



import time
def calcProd():
 # Calculate the product of the first 100,000 numbers.
   product = 1
   for i in range(1, 100000):
      product = product * i
   return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (str(prod)))
print('Took %s seconds to calculate.' % (endTime - startTime))
'''
import time
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
# TODO: Start tracking the lap times.
try:
   while True:
      input()
      lapTime = round(time.time() - lastTime, 2)
      totalTime = round(time.time() - startTime, 2)
      print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
      lapNum += 1
      lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    
