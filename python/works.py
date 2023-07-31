print("What is your name")
name = input()
A= int()
while A >=0:
    print('What is your age')
    A=int(input ())
    if A>=18:
        print("ok")
        print('☺ We will like to obtain informations about yourself as we move forward')
 
        
        print ('What are your physical status')
        print('ok or disabled? ')
        status=input()
        if status=='ok':
            print ('we move on')
        else:
            print('please what was the cause')
            cause=input()
        print ('What are your hobbies')
        hobbies=[ ]
        while True:
                print('Hobby '+ str(len(hobbies) + 1)+' (or type nothing to stop)')
                hob=input()
                if hob==' ' :
                    break
                hobbies=hobbies+[hob]
        print('Your hobbies are:')
        for name in hobbies:
            print('  '+name)
    else:
        print("Access denied") 
        break