#this is a random password generator

import random

def main(n):
   let ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   spec = "!@#$%&*"
   spec = list(spec)
   let=list(let)
   
   p=""
   special=""
   for i in range(7):
      i = random.randint(0,51)
      ip =let[i]
      p=ip + p

   for s in range(3):
      s = random.randint(0,6)
      sp = spec[s]
      special = sp + special
      
   for e in range(6):
      e=random.randint(0,999999)
      
   new_pass=str(e)+ p + special
   ne = ''.join(random.sample(new_pass,len(new_pass)))
   if n <= 16:
      print(ne[:n])
   else:
      print("Characters exceeds maximum limit(0-16)")

main(n)
