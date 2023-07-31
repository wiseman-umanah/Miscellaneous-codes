word = input("TYPE ANY SENTENCE TO OUTPUT THE AVERAGE LENGTH OF THE WORDS:\n")
#this output the average length of the words including the whitespace(s)
w = [(',',''),('.',''),('?','')]
t = word.split()
for o,n in w:
   word = word.replace(o,n)
   
print(len(word)//len(t))

#codeReadyForAccessmentInSololearn
