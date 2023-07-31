birthday={'Chizzy': 'Apr 8','Juliet' : 'Apr 19', 'Ogechi' : 'Feb 26'}
import sys
while True:
    print('Enter name: (Type exit to end program)')
    name= input()
    if name=='exit':
      break
     
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print(name + '\'s'+ ' birthday doesn\'t exist in my database')
        print ('What is their birthday :')
        bday=input ()
        birthday[name]=bday
        print ('Database updated')
sys.exit()
       