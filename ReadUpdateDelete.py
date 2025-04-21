"""
TURN LINE WRAPPING OFF FOR A BETTER VIEW

+-------------------------------------------------------------------+
|            ***------------   MODULE   ------------***             |
|                                                                   |
|                                                                   |
|Author: Raktimjyoti Sarma (RaktimJS)                               |
|Institution: Pathsala Public School, Pathsala, Seuj Nagar, 781325  |
|Date Created: 12/03/2025                                           |
|Email: raktimunreal4@gmail.com                                     |
|                                                                   |
|                                                                   |
|                        DO NOT PLAGIARISE                          |
|                                                                   |
|                                                                   |
| Contains code for Read Update and Delete operations.              |
+-------------------------------------------------------------------+

Last Edited: 30th March, 2025

"""




DEL_LINE = "\033[A\033[K"
WHITE = "\033[38;2;212;212;212m"
YELLOW = "\033[38;2;255;200m"
RED = "\033[38;2;200;0m"
lb = "\033[38;2;108;180;238m"

__import__('os').system('cls')

from tabulate import tabulate

import json
from math import floor as floor




# Setup
def loadJson(jsonFileName:str):
        classData = None
        
        with open("gradesJSON/"+jsonFileName, "r") as existingData:
                classData = json.load(existingData)

        return classData


def selectSubs9and10(subjectList: list):
        optedSubjects = []

        for i in range(len(subjectList)):
                print(subjectList[i], end="")
                
                if i != len(subjectList) - 1:
                        print(",", end=" ")

                if (i+1) % 5 == 0:
                        print("")
        
        print(f"\033[0m{RED}\nYou may choose a maximum of 3 subjects and minimum 1{WHITE}\n")

        k = 0

        while k < 3:
                subject = input(f"Enter the subject from the above list (Type QUIT to quit): {YELLOW}")
                print(WHITE, end="")

                subject = subject.upper()
                subject = " ".join(subject.split())

                if subject in subjectList and subject not in optedSubjects:
                        optedSubjects.append(subject)
                        print(f"{lb}\033[3mSubject added\n{WHITE}\033[0m")

                        k += 1
                elif subject.lower() == 'quit':
                        if len(optedSubjects) >= 1:
                                print("\n")
                                break
                        else:
                                print(f"You must select at least {YELLOW}1{WHITE} subject from this section\n")
                elif subject in optedSubjects:
                        print(f"{YELLOW}{subject}{WHITE} has been added already\n")
                elif not subject.strip():
                        print(f"{DEL_LINE}Enter the subject from the above list (Type QUIT to quit): {YELLOW}\033[3m*BLANK*\033[0m")
                        print("Empty input is not supported\n")
                else:
                        print(f"{YELLOW}{subject}{WHITE} is not available\n")

        return optedSubjects


def selectSubs11and12(subjectList: list):
        print("\033[3m", end="")

        for i in range(len(subjectList)):
                print(subjectList[i], end="")
                
                if i != len(subjectList) - 1:
                        print(",", end=" ")

                if (i+1) % 5 == 0:
                        print("")
        
        print("\033[0m\n")




# CRUD (Create Read Update Delete)

# Create (C)
# Has been made in addNewStudent.py

"""================================================================================"""


# Read (R) ---- 1
def printGradeData(jsonFileName: str, printPartial: bool = True, subject: str = "all"):
        jsonData = loadJson(jsonFileName)
        subject = subject.upper()

        breakAll = False

        if not jsonData:
                print("No data to show")
                return

        for j in jsonData:
                if printPartial == False and jsonData[j]["IsDeleted"] == 'False':
                        if subject.lower() == "all" or not subject.strip():
                                print(f"Roll Number {YELLOW}{jsonData[j]["Roll_No"]}{WHITE},", end=" ")
                                print(jsonData[j]["Name"])

                                data = jsonData[j]["Subjects"]

                                rows = [[key] + [f"{lb}{val}{WHITE}" for val in values.values()] for key, values in data.items()]
                                columns = ["Subjects"] + list(next(iter(data.values())).keys())
                                table = tabulate(rows, columns, tablefmt = "psql")

                                print(table)
                                print("\n\n")

                                breakAll = True
                        elif subject in jsonData[j]["Subjects"]  or not subject.strip():
                                print(f"Roll Number {YELLOW}{jsonData[j]["Roll_No"]}{WHITE},", end=" ")
                                print(jsonData[j]["Name"])

                                print(f"\t{subject} : \n\t\t", end="")

                                for k in jsonData[j]["Subjects"][subject]:
                                        print(f"| {k}{RED} : {YELLOW}{jsonData[j]["Subjects"][subject][k]}{WHITE}", end=" ")

                                print("\n\n")

                                breakAll = True
                        elif subject not in jsonData[j]["Subjects"]:
                                print(f"\n{YELLOW}{subject.upper()}{WHITE} is not a valid subject. Please recheck the word")
                                input("Press enter to continue...")

                                __import__('os').system('cls')

                                break
                else:
                        if subject.lower() == "all" or not subject.strip():
                                        print(f"Roll Number {YELLOW}{jsonData[j]["Roll_No"]}{WHITE},", end=" ")
                                        print(jsonData[j]["Name"])




# Read (R) ---- 2
def printSpecificStudent(jsonFileName:str, rollNumber: int):
        classData = loadJson(jsonFileName)

        if rollNumber <= len(classData) and rollNumber > 0:
                if classData[f"stud{rollNumber}"]["IsDeleted"] == "False":
                        print(f"Roll Number {YELLOW}{classData[f"stud{rollNumber}"]["Roll_No"]}{WHITE},", end=" ")
                        print(classData[f"stud{rollNumber}"]["Name"])

                        data = classData[f"stud{rollNumber}"]["Subjects"]

                        rows = [[key] + [f"{lb}{val}{WHITE}" for val in values.values()] for key, values in data.items()]
                        columns = ["Subjects"] + list(next(iter(data.values())).keys())
                        table = tabulate(rows, columns, tablefmt = "psql")

                        print(table)
                else:
                        print(f"Student with roll number {rollNumber} doesn't exist")
                        break
        else:
                print(f"Student with roll number {rollNumber} doesn't exist")
                break


"""================================================================================"""


# Update (U) ---- 1
def updateName(jsonFileName: str, rollNumber: int, name: str):
        classData = loadJson(jsonFileName)

        for key in classData:
                if classData[key]["Roll_No"] == rollNumber:
                        studentKey = key
                        break

        if classData[f"stud{rollNumber}"]["IsDeleted"] == "False":
                if studentKey:
                        classData[studentKey]["Name"] = name

                        with open("gradesJSON/"+jsonFileName, "w") as updatedData:
                                json.dump(classData, updatedData, indent=8)
                else:
                        print(f"Student record with roll number {YELLOW}{rollNumber}{WHITE} doesn't exist")
        else:
                print(f"Data of student with Roll Number {YELLOW}{rollNumber}{WHITE} is not available")


# Update (U) ---- 2
def updateMarks(jsonFileName: str, rollNumber: int):
        breakLoop = True

        classData = loadJson(jsonFileName)

        while True:
                if rollNumber <= len(classData):
                        for key in classData:
                                if classData[key]["Roll_No"] == rollNumber:
                                        studentKey = key
                                        break
                        
                        if classData[f"stud{rollNumber}"]["IsDeleted"] == "False" and studentKey:
                                print()
                                printSpecificStudent(jsonFileName, rollNumber)

                                while True:
                                        try:
                                                subjectSelector = input(f"\n\nEnter the subject of which you want to update marks: {YELLOW}")
                                                subjectSelector = subjectSelector.upper()
                                                print(f"{WHITE}", end="")

                                                if subjectSelector in classData[studentKey]["Subjects"]:
                                                        print("\n• Re-enter the old mark or leave the field blank to keep it unchanged")
                                                        print("• Unsupported values will be trated as empty values")
                                                        print("• Any value greater than 100 and less than 1000 will converted to the integer closest to its one-tenth")
                                                        print("• Any value greater than or equal to 1000 converted to the 100\n\n")

                                                        print(f"{lb}{subjectSelector}{WHITE}:")

                                                        for i in classData[studentKey]["Subjects"][subjectSelector]:
                                                                while True:
                                                                        try:
                                                                                newMark = input(f"\t{i} (Current marks: {YELLOW}{classData[studentKey]["Subjects"][subjectSelector][i]}{WHITE}) {RED}:{YELLOW} ")
                                                                                print(f"{WHITE}", end="")

                                                                                newMark = float(newMark)

                                                                                if newMark >= 1000:
                                                                                        print(DEL_LINE, end="")
                                                                                        print(f"\t{i} (Current marks: {YELLOW}{classData[studentKey]["Subjects"][subjectSelector][i]}{WHITE}) {RED}: {YELLOW}\033[9m{newMark}\033[0m {YELLOW}100{WHITE}")
                                                                                        newMark = int(100)
                                                                                if newMark > 100 and newMark < 1000:
                                                                                        print(f"{DEL_LINE}\t{i} (Current marks: {YELLOW}{classData[studentKey]["Subjects"][subjectSelector][i]}{WHITE}) {RED}: {YELLOW}\033[9m{newMark}\033[0m {YELLOW}{floor(newMark/10)}{WHITE}")
                                                                                        newMark = float(f"{(newMark/10):.2f}")

                                                                                classData[studentKey]["Subjects"][subjectSelector][i] = newMark
                                                                                break

                                                                        except ValueError:
                                                                                print(f"{WHITE}{DEL_LINE}\t{i} (Current marks: {YELLOW}{classData[studentKey]["Subjects"][subjectSelector][i]}{WHITE}) {RED}: \033[3m{YELLOW}*{classData[studentKey]["Subjects"][subjectSelector][i]}*{WHITE}\033[0m")
                                                                                break

                                                        with open("gradesJSON/"+jsonFileName, "w") as updatedData:
                                                                json.dump(classData, updatedData, indent=8)

                                                elif not subjectSelector.strip():
                                                        print(f"{DEL_LINE}Enter the subject of which you want to update marks: {YELLOW}\033[3m*BLANK*\033[0m")
                                                        print(f"Can't process empty input. Please re-enter\n")
                                                else:
                                                        print(f"Student has no subject named {lb}{subjectSelector}{WHITE}. Please recheck the spelling\n")
                                        except EOFError or ValueError:
                                                print("Invalid Input")
                                        
                                        continuation = input(f"\nDo you want to update marks for another subject? (Y/N) (Arbitrary values will be considered as 'N'): {YELLOW}")
                                        print(WHITE, end="")
        
                                        if continuation.lower() == "y":
                                                pass
                                        else:
                                                breakLoop = True
                                                break

                                if breakLoop == True:
                                        break
                        else:
                                print(f"Data of student with Roll Number {YELLOW}{rollNumber}{WHITE} is not available")
                else:
                        print(f"Student with Roll Number {YELLOW}{rollNumber}{WHITE} doesn't exist")

# Update (U) ---- 3
def updatePassword():
        hasUpper = False
        hasSpecialSymbol = False
        hasDigit = False

        with open("password.json", "r") as xyz:
                pswrdDict = json.load(xyz)
 
        print("\n\nPassword must be at least 8 characters long")
        print("Password must have alteast 1 upper case letter")
        print(f"Password must have alteast 1 special symbol {YELLOW}(_, !, @, #, $, %, &){WHITE}")
        print("Password must have alteast 1 digit\n\n")

        while True:
                pswrd = input(f"\nEnter the new password: {YELLOW}")
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

                                print("\nPassword has been updated!")
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


"""================================================================================"""


# Delete (D) ---- 1
def deleteRecord(jsonFileName: str, rollNumber: int):
        classData = loadJson(jsonFileName)

        if rollNumber <= len(classData) and rollNumber > 0:
                if classData[f"stud{rollNumber}"]["IsDeleted"] == "True":
                        print(f"Student with Roll Number {YELLOW}{rollNumber}{WHITE} doesn't exist")
                else:
                        classData[f"stud{rollNumber}"]["IsDeleted"] = "True"

                with open("gradesJSON/"+jsonFileName, "w") as updatedData:
                        json.dump(classData, updatedData, indent=8)

                print("\nStudent record deleted successfully\n")

                printGradeData(jsonFileName)
        else:
                print(f"Student with Roll Number {YELLOW}{rollNumber}{WHITE} doesn't exist")


# Delete (D) ---- 2
def clearGradeData(jsonFileName):
        print(f"\n{RED}I know that I am deleting all records, and this action can't be undone{WHITE}")

        while True:
                classData = loadJson(jsonFileName)
                confirmation = input(f"Type the text above: {YELLOW}")
                print(WHITE, end="")

                if confirmation == "I know that I am deleting all records, and this action can't be undone":
                        classData.clear()
                        break
                else:
                        pass

        with open("gradesJSON/"+jsonFileName, "w") as updatedData:
                json.dump(classData, updatedData, indent=8)


        print("\nData cleared")

"""================================================================================"""



