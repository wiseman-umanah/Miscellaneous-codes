from importlib.resources import open_text
import os
from os import path 
from os import mkdir

print(os.getcwd())
totalbyte = 0
#get a list of all the files in the current directory
dirlist = os.listdir()
for entry in dirlist:
    #make sure its a file :
    if os.path.isfile(entry):
        #add the file sixe to the total
        filesize = os.path.getsize(entry)
        totalbyte += filesize


#create a subdirectoy called result
os.mkdir("result")

#create output file
resultsfile = open("result/result.txt","w+")
if resultsfile.mode == "w+":
    resultsfile.write("total bytecount:" +str(totalbyte) +"\n")
    resultsfile.write("file list: \n")
    resultsfile.write("------------\n")
    #write the result into the the file
    for entry in dirlist :
        if os.path.isfile(entry):
            #write the file name to the result ledger
            resultsfile.write(entry + "\n")

    #close the file when done 
    resultsfile.close()