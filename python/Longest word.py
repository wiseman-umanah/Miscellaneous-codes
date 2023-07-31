'''Given a text as input, find and output the longest word
sample input
this is an awesome text

sample output
awesome

Recall the split(' ') method,which returns a list of words of the string'''

def main():
   word = 'this is an awesome text'
   word = word.split()
   t  = []
   
   for i in word:
      i = [len(i)]
      t= i + t
   t=max(t)
   
   for r in word:
      if len(r) == t:
         print(r)
         
if __name__ == "__main__":
   main()
