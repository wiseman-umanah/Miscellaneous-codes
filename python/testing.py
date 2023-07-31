'''word = input("TYPE ANY SENTENCE TO OUTPUT THE AVERAGE LENGTH OF THE WORDS:\n")
#this output the average length of the words including the whitespace(s)
w = ''
t = word.split()
for o in word:
   if o.isalpha() or o.isspace():
      w += o
print(len(w)//len(t))  
'''
import os,shutil
number = 0
source = "C:\\Users\\Wiseman\\Pictures"
for i in os.listdir(source):
   i =  "C:\\Users\\Wiseman\\Pictures\\" + i
   if i.startswith("IMG"):
      number=number +1
      new="C:\\Users\\Wiseman\\Pictures\\PIC"+str(number)+".jpg"
      shutil.move(i, new)
      print("done")
