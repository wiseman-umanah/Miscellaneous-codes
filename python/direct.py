#! python3

import os, shutil
source = "C:\\Users\\Wiseman\\Downloads"
images = "C:\\Users\\Wiseman\\Pictures" #png,bmp,jpg,jpeg
videos ="C:\\Users\\Wiseman\\Videos" #mkv,mp4
musics = "C:\\Users\\Wiseman\\Documents\\music" #mp3,m4a
software = "C:\\Users\\Wiseman\\Documents\\software" #softwares


def move():
   sor = os.listdir(source)
   print(sor)
   for i in sor:
      i = "C:\\Users\\Wiseman\\Downloads\\" + i
      if i.endswith("mp3") | i.endswith("m4a"):
         shutil.move(i,musics)
         print(" MUSIC FOUND")
      elif i.endswith("mkv") |  i.endswith("mp4") | i.endswith("avi"):
         shutil.move(i,videos)
         print("VIDEO FOUND")
      elif i.endswith("png") | i.endswith("bmp") | i.endswith("jpeg") | i.endswith("JPEG") | i.endswith("jpg") | i.endswith("JPG"):
         shutil.move(i,images)
         print("IMAGE FOUND")
      elif i.endswith("exe"):
         shutil.move(i,software)
         print("SOFTWARE FOUND")
     
      else:
         pass
   print("\nDONE")
move()
