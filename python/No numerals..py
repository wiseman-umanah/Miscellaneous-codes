'''You write a phrase and include a lot of number characters(0-9),
but you decide that for numbers 10 and under you would rather write the word out,
can you go in and edit your phrase to write out the name of each number instead of using
the numerals
task:
take a phrase and replace any instances of using an integer from 0 - 10 and replace it with the
English word that corresponds to that integer
Input:
A string of the phrase in its normal form

Output:
A string of the updated phrase that has changed all numerals to English word

Sample input:
i need 2 pumpkins and 3 apples

sample Output:
i need two pumpkin and 3 apples
'''
word = 'I need 2 pumpkins and 3 apples'
word= word.lower()
replace = [('0','zero'),('1',"one"),("2","two"),("3","three"),("4","four"),("5","five"),("6","six"),("7","seven"),("8","eight"),("9","nine"),("10","ten")]
for i,d in replace:
   word = word.replace(i,d)

print(word)
