
from datetime import datetime
from datetime import time
from datetime import date
import random

def stam():
   print("OPAY POS OPAY v.1.4")
   print("ng-pos-issue@opay.com")

def main():
   print("\nMCH NAME: OPAY/UYO")
   print("TID: 20572X20")
   print("SN : 9121101490" + str(SN1))
   print("\n---------CUSTOMER-----------\n")
   print("     ",Acct_type,"\n" )
   print("     ", PAYMENT)
   print("Amount : NGN", amt)
   print("--------------------------")
   print("Transaction Approved")
   print("Recipient Account :" , account)
   print("Recipient Account Name :", name)
   print (time)
   print("-------------------")
   stam()

def air():
   print("\nMCH NAME: OPAY/UYO")
   print("TID: 20572X20")
   print("SN : 9121101490" + str(SN1))
   print("\nNetwork:",net )
   print("Amount : NGN", amt)
   print("--------------------------")
   print("Successful recharge")
   print("\nRecipient Account :" , account)
   print("Recipient Account Name :", name)
   print (time)
   print("-------------------")
   stam()

def acc():
   print("\nMCH NAME: OPAY/UYO")
   print("TID: 20572X20")
   print("SN : 9121101490" + str(SN1),"\n")
   print("BANK:",bank.upper(),"\n" )
   print("ACCOUNT NAME:",acctname)
   print("ACCOUNT NUMBER:",acctnum)
   print("--------------------------")
   print("Account successfully created\n")
   print("Recipient Account :" , account)
   print("Recipient Account Name :", name)
   print (time)
   print("-------------------")
   stam()

def tran():
   print("\nAgent:\t ", name)
   print("BANK:\t ",bank.upper())
   print("ACCOUNT NUMBER:\t  ******"+acc[5:])
   print("Terminal ID:\t  20572X20")
   print("Agent's ID:\t 9121101490" + str(SN1))
   print("--------------------------")
   print("Sender's name:\t",sender)
   print("Sender's number:\t",sendnum)
   print("--------------------------")
   print("Transaction successful")
   print("Amount:\t",amt)
   print("--------------------------")
   print (time)
   stam()



run = True
while(run):
   try:
      print ("\nWELCOME!")   
      print("Type exit to close or press any key to continue")

      respond = input()
      if respond == "exit":
         exit()

      else:        
         print("INPUT Name of Account")
         name = input()

      while True:
         print("INPUT Account number")
         account = input()
         if len(account) == 10:
            account = int(account)
            break
         else:
            print("Account number not correct")
      
      
      p = ("FUND TRANSFER","CASH DEPOSIT","CASH WITHDRAWAL","BILL PAYMENT","ACCOUNT OPENING","AIRTIME PURCHASE")
      SN1 = random.randint(0000,9999)
      print("What do you want to do?")
      for i,d in enumerate(p):
        print(i,":",d)
      PAYMENT = int(input())

            
      if PAYMENT == 4:
         PAYMENT = p[PAYMENT]
         bank = input("Which bank are you interested in\n")
         acctname = input("Input your account name(First name and Last name)\n")
         acctnum = random.randint(0000000000,9999999999)
         time = datetime.now()
         acc()
         
      elif PAYMENT == 5:
         PAYMENT = p[PAYMENT]
         net = input("Which network do you want to purchase\n")
         amt = int(input("How much\n"))
         time = datetime.now()
         air()

      elif PAYMENT ==  0:
         PAYMENT = p[PAYMENT]
         print("Please input the account number of the receiver")
         while True:
            acc= input()
            if len(acc) == 10:
               break
            else:
               print("Account number not correct")
         print("Name of bank")
         bank = input()
         sender = input("Sender's name: ")
         sendnum = input("Sender's number: ")
         print("How much are you transferring")
         amt = int(input())
         time = datetime.now()
         tran()

      elif PAYMENT ==  1 or 2 or 3 :
         PAYMENT = p[PAYMENT]
         print("Please select your Account type")
         acct = ("Saving Account","Current Account")
         for i, e in enumerate(acct):
            print(i,":",e)
         Acct_type = int(input())
         Acct_type = acct[Acct_type]
         print("How much are you ")
         amt = int(input())
         time = datetime.now()
         if __name__ == "__main__":
            main()




         
   except Exception as e:
      print(e)
      print("Sorry invalid input")
      print("TRANSACTION ERROR")


