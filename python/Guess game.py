#This is a guess the number game.
import random
secretNumber= random. randint(1,20)
print('Player\'s name')
player=str(input ())
print('I am thinking of a number between 1 and 20. ')

#Ask the player to guess 6 times.
print ('You are allowed to guess only 6 times')
for guessesTaken in range(1,7):
    print('Take a guess. ')
    guess=int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #This condition is the correct guess!

if guess==secretNumber:
    print('Good job! You guessed my number in '+str(guessesTaken)+' guess. ')
else:
    print('Nope. The number i was thinking of was '+str(secretNumber))