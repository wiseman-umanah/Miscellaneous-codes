print('\n \tEnter your encrypted code: ')
message=str(input())
for c in message[::-1]:
  if c.isalpha() or c.isspace():
    print (c, end='')