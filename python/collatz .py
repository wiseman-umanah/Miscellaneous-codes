def collatz(number):
    run  =True
    while run:
        if number % 2 ==0:
            number = number//2
            print(number)
        elif number % 2 !=0:
            number = 3* number + 1
            print(number)
        if number <= 0:
            print(str(number),"Not supported in this sequence")
            run = False
        if number == 1:
            run = False
while True:            
    try:                  
            number = int(input("Enter an integer(n>0)\n"))
            collatz(number)
    except Exception as e:
        print('An error happened:',str(e))

