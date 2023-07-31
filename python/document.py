#! python3
import os,shutil
source = "C:\\Users\\Wiseman\\Documents"
docs = "C:\\Users\\Wiseman\\Documents\\WORD"
sheets = "C:\\Users\\Wiseman\\Documents\\EXCEL"
software = "C:\\Users\\Wiseman\\Documents\\software" #softwares
pdfs = "C:\\Users\\Wiseman\\Documents\\Books"
graphics = "C:\\Users\\Wiseman\\Documents\\Corel"

def move():
   sor = os.listdir(source)
   for i in sor:
      i = "C:\\Users\\Wiseman\\Documents\\" + i
      if i.endswith("docx"):
         shutil.move(i,docs)
         print(" DOC FOUND")
      elif i.endswith("xlsx"):
         shutil.move(i,sheets)
         print("SPREADSHEET FOUND")
      elif i.endswith("exe"):
         shutil.move(i,software)
         print("SOFTWARE FOUND")
      elif i.endswith("pdf"):
         shutil.move(i,pdfs)
         print("PDF FOUND")
      elif i.endswith("cdr"):
         shutil.move(i,graphics)
         print("GRAPHIC FOUND") 
      else:
         #print(os.path.getsize(i))
         #print(os.path.basename(i),"can't be moved with such extension")
         pass
   print("\nDONE")
move()
