'''You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in the same order except that you take the first letter of each word and put it on the end,
then you add 'ay' to the end of that. ("road" = "oadray") 

Task
Your task is to take a sentence in English and turn it into the same sentence in Pig Latin! 

Input Format 
A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization)

Output Format 
A string of the same sentence in Pig Latin.

Sample Input 
"nevermind you've got them"

Sample Output 
"evermindnay ou'veyay otgay hemtay"
'''
#Takes input
word = input()

#Empty string 
t = ""

#Remove any punctuation
for p in word :
   if p.isspace() or p.isalpha():
      t = t+p #save the unpuctuated string in empty string to be used later

#change all CAPS to smallcase - no capitalization
word = t.lower()

#split words into list 
wordList = word.split()

#loop over each word to be formatted to piglatin
for i in wordList:
   x=list(i)
   temp=x[-1]+x[0] + "ay"
   x[0]=""
   x[-1]=temp
   x = "".join(x)
   print(x,end = " ")
'''

x=list(string)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))
def swap(string):
     
    # storing the first character
    start = string[0]
     
    # storing the last character
    end = string[-1]
     
    swapped_string = end + string[1:-1] + start
    print(swapped_string)
     
# Driver Code
swap("GeeksforGeeks")
swap("Python")
'''   
