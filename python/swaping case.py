#Write a code that takes any sentence as input and swaps the case
#(i.e uppercase becomes lowercase and vice versa )
#

n = "Alien War Zone"
for i in n:
   if i==i.upper():
      i=i.lower()
      #print(i)
      print(i,end='')
   elif i == i.isspace():
      i = " "
      print(i,end='')
   elif i == i.lower():
      i=i.upper()
      print(i,end='')
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(arr)

# def split_and_join(line):
#     a = line.split(" ")
#     a = '-'.join(a)
#     return a
#     write your code here
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
