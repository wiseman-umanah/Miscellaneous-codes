letters = " abcdefghijklmnopqrstuvwxyz "
letters = list(letters)
w = input("input your message to translate it backwards\n")
w = w.lower()
for i in w:
      if i.isalpha() or i.isspace(): #Removes any special character including numbers that is not an alphabet that may cause an error
            t = letters[abs(letters.index(i)- 27)] 
            print(t,end = "")
