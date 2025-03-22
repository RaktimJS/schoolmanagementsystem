"""
TURN LINE WRAPPING OFF FOR A BETTER VIEW

+-------------------------------------------------------------------+
|            ***------------   MODULE   ------------***             |
|                                                                   |
|                                                                   |
|Author: Raktimjyoti Sarma (RaktimJS)                               |
|Institution: Pathsala Public School, Pathsala, Seuj Nagar, 781325  |
|Date Created: 09/03/2025                                           |
|Email: raktimunreal4@gmail.com                                     |
|                                                                   |
|                                                                   |
|                        DO NOT PLAGIARISE                          |
|                                                                   |
|                                                                   |
| Contains code that work as UI elements in 'script.py'.            |
+-------------------------------------------------------------------+

Last Edited: 19th March, 2025

"""




import os
import ReadUpdateDelete as rud
from addNewStudent import addNewStudent

DEL_LINE = "\033[A\033[K"
WHITE = "\033[38;2;212;212;212m"
YELLOW = "\033[38;2;255;200;0m"
RED = "\033[38;2;200;0;0m"
lb = "\033[38;2;142;238;190m"




def ui(jsonFileName: str):
        print(f"\n{'='*90}\n")

        print("Do you want to clear the screen before continuing?")
        print(f"Enter '{YELLOW}Y{WHITE}' for YES or '{YELLOW}N{WHITE}' for NO")
        print(f"\n{RED}Any other values will be treated as '{YELLOW}N{WHITE}'")

        while True:
                clsBool = input(f"\nEnter your choice: {YELLOW}")
                print(f"{WHITE}", end="")

                if clsBool.lower() == 'y':
                        os.system('cls')
                        break
                elif clsBool == 'n':
                        break
                else:
                        print("Invalid Input")


        if clsBool != "y":
                print(f"\n{'~'*35}\n")
        else:
                print("\n\n")
        
        print(f"{lb}CLASS {jsonFileName.split("grade")[1].split(".json")[0]}\n\n{WHITE}")

        print(f"Enter {YELLOW}1{WHITE} to SEE BASIC STUDENT DETAILS")
        print(f"Enter {YELLOW}2{WHITE} to SEE EXAM DETAILS OF THE WHOLE CLASS")
        print(f"Enter {YELLOW}3{WHITE} to SEE EXAM DETAILS FOR ONE SUBJECT OF THE WHOLE CLASS")
        print(f"Enter {YELLOW}4{WHITE} to ADD A NEW STUDENT")
        print(f"Enter {YELLOW}5{WHITE} to UPDATE STUDENT'S NAME")
        print(f"Enter {YELLOW}6{WHITE} to UPDATE STUDENT'S MARKS")
        print(f"Enter {YELLOW}7{WHITE} to DELETE A STUDENT'S RECORD\n")
        print(f"{YELLOW}IRREVERSIBLE ACTION:{WHITE}")
        print(f"Enter {YELLOW}8{WHITE} to {RED}DELETE ALL RECORDS{WHITE}\n\n")

        print(f"TYPE '{YELLOW}QUIT{WHITE}' TO QUIT")

        while True:
                operationSelector = input(f"\n\nEnter your choice from the above list: {YELLOW}")
                print(WHITE, end="")

                operationSelector.replace(" ","")

                if operationSelector.lower() == 'quit':
                        print("\nTHANK YOU!")
                        break
                elif operationSelector.lower() != "quit" and operationSelector not in '12345678':
                        print("Invalid Input. Try again")
                elif not operationSelector.strip() == True and operationSelector not in '12345678':
                        print("Invalid Input. Try again")
                else:
                        operationSelector = int(operationSelector)
                        break
                
        if operationSelector == 1:
                print(f"\n\n{'~^'*35}\n\n")

                rud.printGradeData(jsonFileName, True)
        elif operationSelector == 2:
                print(f"\n\n{'~^'*35}\n\n")

                rud.printGradeData(jsonFileName, False)
        elif operationSelector == 3:
                print(f"\n\n{'~^'*35}\n\n")

                subject = input(f"Enter the subject you want to view marks for: {YELLOW}")
                print(WHITE, end="")

                rud.printGradeData(jsonFileName, False, subject)
        elif operationSelector == 4:
                print(f"\n\n{'~^'*35}\n\n")

                addNewStudent(jsonFileName)
        elif operationSelector == 5:
                print(f"\n\n{'~^'*35}\n\n")

                while True:
                        try:
                                rollNumber = input(f"Enter roll no. of the student whose mark(s) is(are) to be edited: {YELLOW}")
                                print(WHITE, end="")

                                rollNumber = int(rollNumber)

                                break
                        except ValueError or EOFError:
                                print("Invalid Input\n")

                newName = input(f"Enter the new name: {YELLOW}")
                print(WHITE, end="")

                rud.updateName(jsonFileName, rollNumber, newName)
                rud.printSpecificStudent(jsonFileName, rollNumber)
        elif operationSelector == 6:
                print(f"\n\n{'~^'*35}\n\n")

                while True:
                        try:
                                rollNumber = input(f"Enter roll no. of the student whose name is to be edited: {YELLOW}")
                                print(WHITE, end="")

                                rollNumber = int(rollNumber)

                                break
                        except ValueError or EOFError:
                                print("Invalid Input\n")

                rud.updateMarks(jsonFileName, rollNumber)
        elif operationSelector == 7:
                print(f"\n\n{'~^'*35}\n\n")

                while True:
                        try:
                                rollNumber = input(f"Enter roll no. of the student whose data is to be deleted: {YELLOW}")
                                print(WHITE, end="")

                                rollNumber = int(rollNumber)

                                break
                        except ValueError or EOFError:
                                print("Invalid Input\n")
                        
                rud.deleteRecord(jsonFileName, rollNumber)
        elif operationSelector == 8:
                print(f"\n\n{'~^'*35}\n\n")

                rud.clearGradeData(jsonFileName)



