def word(x):
   if x.isalnum or x.isalpha:
       print(x == x[::-1])

import sys 
"""A Palindrome is a string that has the same property of reading
the same forwards as it does backwards"""  
while True:      
   print("\nHello") 
   x = input("Please input any word to check if it is a palindrome(Type exit to close program):")
   x = x.lower()
   if x == 'exit' :
      break
   word(x)
      
sys.exit()   
