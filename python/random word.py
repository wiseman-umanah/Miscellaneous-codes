import random
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter = list(letter)
messages=['ur stupid', 
                  'crazy', 
                  'bitch', 
                  'sucker', 
                  'fuck', 
                  'ahh', 
                  'idiot', 
                  'madmaniihig', 
                  'ishi',]
for mesages in range(7):
    print(messages[random.randint(0,len(messages)-1)])

for i in range(4):
    i = random.randint(0,10)
    print(i)
