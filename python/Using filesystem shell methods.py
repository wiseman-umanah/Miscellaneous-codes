import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
def main ():
    # make a duplicate of an existing file
    if path.exists("newfile.txt"):
        #get the path to the file in the current directory
        src = path.realpath("newfile.txt")

        #lets make a backup copy by appending 'bak' to the name
       # dst = src + ".bak"
       # shutil.copy(src, dst)

        #rename the original file
        #os.rename("textfile.txt", "Renamedfile.txt")
        # now put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        #more fine grained control over ZIP files
        with ZipFile("zippy.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("Renamedfile.txt")








if __name__ == "__main__":
    main()