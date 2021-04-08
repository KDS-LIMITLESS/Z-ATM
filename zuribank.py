import sys
import random
from datetime import datetime
from zuridb import ZURIDB


class ZuriAtm():
    db = ZURIDB
    currentBalance = 0
    current_date = datetime.now().strftime("%a %b %d,%H:%M")
    naira = u'\u20A6'
    

    def __init__(self) -> None:
        self.login = ZuriAtm.login(ZuriAtm)


    def generateAccountNumber(self):
       return random.randrange(0000000000, 9999999999)

    def register(self):
        self.accountNumber = self.generateAccountNumber(ZuriAtm)
        try:
            self.username = str(input("Enter your name \n >>> "))

            password = int(input("Enter your password \n >>> "))
        except ValueError:
            print("password must be digits(0-9) not letters")
            sys.exit()
        
        self.db[self.accountNumber] = [self.username, password]
        #print(self.db)
        print(f"Account created successfully! \n Your account number is {self.accountNumber}")
        return self.verify_user_login(ZuriAtm)


    def transactions(self):
       
        print("1.           Withdrawal      ")
        print("2.           Deposit      ")
        print("3.           Complaints      ")
        print("8.           Cancel      ")

        try:
            resp = int(input(">>> "))
            if resp == 1:
                print("How much would you like to withdraw?")
                response = int(input(">>> "))
                print("Take your cash.")
                sys.exit() 

            elif resp == 2:
                print("How much would you like to deposit")
                response = int(input(">>> "))
                naira = u'u\20A6'
                print(
                  "Your current balance is ",\
                      end=f'{self.naira}{self.currentBalance + response}'
                )
                sys.exit()

            elif resp == 3:
                print("What issue would you like to report?")
                response = input(">>> ")
                print("Thank you for contacting us.")
                sys.exit()

            elif resp == 8:
                print("Thank you for choosing ZuriBank!")
                sys.exit()

            else:
                print("Invalid Input! Please Try Again.")
                self.transactions(ZuriAtm)
        except ValueError:
            print("Reply with digits of desired choice ")
            self.transactions(ZuriAtm)

    
    def verify_user_login(self):
        accountNumber = int(input("Enter your account number >>> "))
        password = int(input("Enter your password >>> "))

        print()
        userPSW = {u:p[1] for (u,p) in self.db.items()}

        if not accountNumber in userPSW.keys() or password != userPSW[accountNumber]:
            print("Error: Invalid User Credidentials")
    
            print( 
                " 1. TRY AGAIN", "\n", 
                "2. Register", "\n", 
                "8. Exit"
            )
            resp = int(input(">>> "))
            if resp == 1:
                self.verify_user_login(ZuriAtm) # recursion 
            elif resp == 2:
                self.register(ZuriAtm)
            elif resp == 8:
                print("Have a nice day!")
                exit()
            else:
                print("Invalid Input! Please Try Again")

        username = {u:p[0] for (u,p) in self.db.items()}
        print(f"                 {self.current_date}                  ")
        print(f"Welcome {username[accountNumber]}")
        print("********** What would you like to do? **********")
        return self.transactions(ZuriAtm)

        
    def login(self):

        print("\n", "**********  WELCOME TO ZURIBANK ATM **********", "\n")
        print(f" 1.   Open Account", "\n", "2.   Login")

        resp = int(input(">>> "))

        if resp == 1:
            return self.register(ZuriAtm)
        
        elif resp == 2:
            self.verify_user_login(ZuriAtm)
            
    
ZuriAtm()
    
