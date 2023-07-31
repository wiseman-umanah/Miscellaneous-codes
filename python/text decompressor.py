''' example - a2 b2 = aabb'''
word = 'j2jx3nxik4s5'
word = list(word)
newWord = ""
for i in word:
   if i.isdigit():
      decompressing = (word[(word.index(i)) - 1] * (int(i) - 1))
      newWord += decompressing
   else:
      newWord += i 
print(newWord)
