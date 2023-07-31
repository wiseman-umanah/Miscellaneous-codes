'''def main():
    # Open a file for writing and create if it doesn't exist
    myfile = open("newfile.txt", "w+")

    #Open the file for appending tect to the end 
    myfile = open("newfile.txt","a+")

    #write some lines of data to the file 
    for i in range(10):
         myfile.write ("This is some new text\n")
    
    #close the file when done
    #myfile.close() 

    #Open the file back up and read contents
    myfile = open("textfile.txt", 'r')
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)
        fl = myfile.readlines()
        for x in fl:
         print(x)

        
if __name__ == "__main__" :
    main()'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
def factorial(n):
     logging.debug('Start of factorial(%s%%)' % (n))
     total = 1
     for i in range(n + 1):
         total *= i
         logging.debug('i is ' + str(i) + ', total is ' + str(total))
     logging.debug('End of factorial(%s%%)' % (n))
     return total
print(factorial(5))
logging.debug('End of program')
