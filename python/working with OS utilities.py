#working with OS utilities
#importing os modules and datetime modules

import os
from os import path
import datetime
from datetime import date , time , timedelta
import time


def main():
    #printing name of OS
    print(os.name)

    #checking for item's existence in os and type 
    #print("Item exists:" , str(path.exists("textfile.txt")))
    #print("Item is a file:" , path.isfile("textfile.txt"))
    #print("Item is a directory:" , path.isdir("textfile.txt"))

    #work with file path
    #print("Item's path:" , path.realpath("textfile.txt"))
   # print("Item's path and name:", path.split(path.realpath("textfile.txt")))

    #Getting the modification time
    t = time.ctime(path.getmtime("newfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("newfile.txt")))





if __name__ == "__main__" :
    main()