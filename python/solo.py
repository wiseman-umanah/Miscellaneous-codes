file = open("books.txt","r")
if file.mode == "r":
   f1 = file.readlines()
for t in f1:
   if t != f1[-1]:
      print(t[0] [0] + str(len(t) - 1))
   else:
      print(t[0] [0] + str(len(t)))


'''n = int(input())
for i in range(n):
   t = int(input())
   if t % 2 != 0:
      continue
   else:
      print(sum(t))
'''
