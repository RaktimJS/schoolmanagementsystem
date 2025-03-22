# School Management System
# Date Created: 05/03/2025
# Last Edited: 22nd March, 2025




import time
import json

from os import system
from functionControl import ui
from licenseAndInfo import info
from ReadUpdateDelete import updatePassword as updtPswrd

def timer(s):
        while s: 
                time.sleep(1)
                s -= 1

system('cls')



try:
        DEL_LINE = "\033[A\033[K"
        WHITE = "\033[38;2;212;212;212m"
        YELLOW = "\033[38;2;255;200;0m"
        RED = "\033[38;2;200;0;0m"
        lb = "\033[38;2;108;180;238m"
        LIGHT_YELLOW = "\033[38;2;255;224;110m"

        B = "\033[1m"
        R = "\033[0m"

        continuationSelector = ''

        system('cls')

        hasUpper = False
        hasSpecialSymbol = False
        hasDigit = False

        isPasswordCorrect = False


        with open("password.json", "r") as xyz:
                pswrdDict = json.load(xyz)

        if pswrdDict["isPswrdSet"] == False:
                print("\n\nPassword must be at least 8 characters long")
                print("Password must have alteast 1 upper case letter")
                print(f"Password must have alteast 1 special symbol {YELLOW}(_, !, @, #, $, %, &){WHITE}")
                print("Password must have alteast 1 digit\n\n")

                while True:
                        pswrd = input(f"\nEnter a password: {YELLOW}")
                        print(f"{WHITE}", end="")

                        i = 0

                        if len(pswrd) >= 8:
                                for i in pswrd:
                                        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and hasUpper == False:
                                                hasUpper = True
                                                i = 0
                                        
                                for i in pswrd:
                                        if i in "_!@#$%&" and hasSpecialSymbol == False:
                                                hasSpecialSymbol = True
                                                i = 0
                                        
                                for i in pswrd:
                                        if i in "1234567890" and hasDigit == False:
                                                hasDigit = True
                                                i = 0

                                if hasUpper == True and hasSpecialSymbol == True and hasDigit == True:
                                        pswrdDict["password"] = pswrd
                                        pswrdDict["isPswrdSet"] = True

                                        with open("password.json", "w") as xyz:
                                                json.dump(pswrdDict, xyz, indent = 8)

                                        print("\nPassword has been set!")
                                        isPasswordCorrect = True

                                        break
                                else:
                                        if hasUpper == False:
                                                print(f"{lb}Password must have alteast 1 upper case letter{WHITE}")
                                        if hasSpecialSymbol == False:
                                                print(f"{lb}Password must have alteast 1 special symbol {YELLOW}(_, !, @, #, $, %, &){WHITE}")
                                        if hasDigit == False:
                                                print(f"{lb}Password must have at least 1 number{WHITE}")
                        else:
                                print(f"{lb}Pasword must be at least 8 characters long{WHITE}")
        else:
                for i in range(3):
                        pswrd = input(f"Password (Attempt {i+1} of 3): {YELLOW}")
                        print(f"{WHITE}", end="")

                        with open("password.json", "r") as xyz:
                                pswrdDict = json.load(xyz)

                        if pswrdDict["password"] == pswrd:
                                isPasswordCorrect = True
                                break
                        else:
                                print(f"{lb}Invalid password{WHITE}\n")
                                isPasswordCorrect = False

        if isPasswordCorrect == True:
                print("Welcome!")
                timer(3)
                system("cls")

                while True:
                        if continuationSelector == 'cls' or continuationSelector == '':
                                print(f"\n\n{B}School Manager V1.0{R}\n\n")

                                print(f"Enter  {lb}1{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}1{WHITE}")
                                print(f"Enter  {lb}2{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}2{WHITE}")
                                print(f"Enter  {lb}3{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}3{WHITE}")
                                print(f"Enter  {lb}4{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}4{WHITE}")
                                print(f"Enter  {lb}5{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}5{WHITE}")
                                print(f"Enter  {lb}6{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}6{WHITE}")
                                print(f"Enter  {lb}7{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}7{WHITE}")
                                print(f"Enter  {lb}8{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}8{WHITE}")
                                print(f"Enter  {lb}9{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}9{WHITE}")
                                print(f"Enter {lb}10{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade {YELLOW}10{WHITE}")
                                print(f"Enter {lb}11{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade {YELLOW}11{WHITE}")
                                print(f"Enter {lb}12{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade {YELLOW}12{WHITE}\n")

                                print(f"Enter {lb}13{WHITE} {LIGHT_YELLOW}→{WHITE} See {YELLOW}LICENSE AND PROJECT INFO{WHITE}")
                                print(f"Enter {lb}14{WHITE} {LIGHT_YELLOW}→{WHITE} Change Password\n")

                                print(f"\n{RED}Any exceeding values will be clipped to the closest limit{WHITE}\n")
                        while True:
                                try:
                                        listSelector = input(f"Enter your choice: {YELLOW}")
                                        print(WHITE, end="")
                                        listSelector = int(listSelector)

                                        if listSelector == 1:
                                                ui("grade1.json")
                                        elif listSelector == 2:
                                                ui("grade2.json")
                                        elif listSelector == 3:
                                                ui("grade3.json")
                                        elif listSelector == 4:
                                                ui("grade4.json")
                                        elif listSelector == 5:
                                                ui("grade5.json")
                                        elif listSelector == 6:
                                                ui("grade6.json")
                                        elif listSelector == 7:
                                                ui("grade7.json")
                                        elif listSelector == 8:
                                                ui("grade8.json")
                                        elif listSelector == 9:
                                                ui("grade9.json")
                                        elif listSelector == 10:
                                                ui("grade10.json")
                                        elif listSelector == 11:
                                                ui("grade11.json")
                                        elif listSelector == 12:
                                                ui("grade12.json")
                                        elif listSelector == 13:
                                                info()
                                        elif listSelector == 14:
                                                updtPswrd()
                                        elif listSelector < 1:
                                                listSelector = 1
                                                ui("grade1.json")
                                        elif listSelector > 14:
                                                listSelector = 14
                                                updtPswrd
                                        
                                        break
                                except ValueError:
                                        if not str(listSelector).strip():
                                                print(f"{DEL_LINE}Enter your choice: {YELLOW}\033[3m*BLANK*\033[0m{WHITE}")
                                                print("Invalid Input\n")
                                        else:
                                                print("Invalid Input\n")



                        if listSelector != 13:
                                print(f"\n\nType '{YELLOW}END{WHITE}' TO EXIT")
                                print(f"Type '{YELLOW}CLS{WHITE}' to clear screen and continue")
                                print(f"Hit the {YELLOW}ENTER KEY{WHITE} to continue without clearing screen")

                                continuationSelector = input(f"\nEnter your choice: {YELLOW}")
                                print(f"{WHITE}", end="")

                                if continuationSelector.lower() == 'end':
                                        for i in range (1, 4):
                                                print(f"TERMINATING IN {YELLOW}{4 - i}{WHITE}")
                                                timer(1)
                                                print(DEL_LINE, end="")
                                        system('cls')
                                        break
                                elif continuationSelector.lower() == 'cls':
                                        for i in range (1, 4):
                                                print(f"Continuing after clearing terminal in {YELLOW}{4 - i}{WHITE}")
                                                timer(1)
                                                print(DEL_LINE, end="")
                                        
                                        print("------------------------------------------------------------------------------\n\n\n")
                                        system('cls')
                                elif continuationSelector == '':
                                        print(DEL_LINE, end="")
                                        print(f"Enter your choice: {YELLOW}*BLANK*{WHITE}")
                                        print(f"Continuing without clearing the screen")
                                        print("------------------------------------------------------------------------------\n\n\n")
                                        timer(3)        
                                else:
                                        for i in range (1, 4):
                                                print(f"Invalid input. Terminating in {YELLOW}{4 - i}{WHITE}")
                                                timer(1)
                                                print(DEL_LINE, end="")
                                        system('cls')
                                        break
        else:
                print(f"{RED}Out of tries{WHITE}")
except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to continue")



