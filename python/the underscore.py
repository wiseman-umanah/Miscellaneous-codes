''' Write a program that changes to the required output 
sample input
someEggs

sample output
some_eggs
'''
n = input()
t = list(n)
for i in t :
   if i == i.lower():
      print(i,end = "")
   elif i == i.upper():
      i = "_"+ i.lower()
      print(i,end = "")

      
