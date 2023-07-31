def is_palindrome(teststr):
   # use the slice trick to reverse the string
   if teststr == teststr[::-1]:
      return True
   return False

run = True
while(run):
   teststr = input("Enter string to test for palindrome or 'exit' :")
   
   #if the user types "exit" then quit the program
   if teststr == "exit":
      run = False
      break
   #convert the string to all lowercase
   teststr = teststr.lower()
   
   #strip all the spaces andpuntuation from thestring 
   newstr = ""
   for x in teststr:
      if x.isalnum():
         newstr += x
   print("Palindrome test :",  is_palindrome(newstr))
