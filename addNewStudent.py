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
| Contains code for taking new student entries. Dynamically detects |
| grade, considering the name of the JSOn storing the data of that  |
| particular grade matches the hardcoded naming format              |
+-------------------------------------------------------------------+

Last Edited: 19th March, 2025

"""




DEL_LINE = "\033[A\033[K"
WHITE = "\033[38;2;212;212;212m"
YELLOW = "\033[38;2;255;200;0m"
RED = "\033[38;2;200;0;0m"
lb = "\033[38;2;142;238;190m"




import json

from ReadUpdateDelete import loadJson
from ReadUpdateDelete import printSpecificStudent
from ReadUpdateDelete import selectSubs9and10
from ReadUpdateDelete import selectSubs11and12




def addNewStudent(jsonFileName: str):
        grade = jsonFileName.split(".")[0].split("grade")[1]
        grade = int(grade)


        if grade >= 1 and grade <= 3:
                while True:
                        studentName = input(f"Enter Student's Name: {YELLOW}")
                        print(f"{WHITE}", end="")

                        if len(studentName) >= 1:
                                break
                        else:
                                print("Invalid Input")

                classData = loadJson(jsonFileName)
                newStudNum = len(classData) + 1

                print("\nDo you want to populate student's marks?")
                print("All marks will be set to 0 by default, if chosen 'NO', or left blank\n")
                
                try:
                        populateMarksBool = input(f"Enter 'Y' for YES and 'N' for NO {RED}(Other values will be considered 'NO'): {YELLOW}")
                        print(f"{WHITE}", end="")
                except populateMarksBool.lower() != "y" or populateMarksBool.lower() != "n" or EOFError:
                        populateMarksBool = "n"

                newMarks = {
                        "Math": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "EVS": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Lang1": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Lang2": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Lang3": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Computer": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "GK": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                }

                if populateMarksBool.lower() != "y" :
                        if populateMarksBool != "n":
                                print(f"{DEL_LINE}Enter 'Y' for YES and 'N' for NO "
                                f"{RED}(Other values will be considered 'NO')"
                                f": {YELLOW}*UNSUPPORTED VALUE*{WHITE}")
                        print("\nThank you! Marks for all subjects for all assessments has been set of zero."
                        " You can edit them later!")
                else:
                        print("\nEnter the marks in the order: ")
                        print(f"\n\t{YELLOW}[FA1, FA2, SA1, FA3, FA4, SA2]{WHITE}\n")
                        print("Enter them in comma seperated values. [Eg: 100, 88, 95, 79, 81]")

                        print(f"\nAny value greater than {YELLOW}100{WHITE} and less than {YELLOW}999{WHITE} will be made one tenth (Eg: {YELLOW}885{WHITE} will be converted to {YELLOW}88.5{WHITE})")
                        print(f"Any value greater than {YELLOW}1000{WHITE} will be considered {YELLOW}100{WHITE}\n")

                        print(f"{RED}Arbitrary values will throw you back to the input\n{WHITE}")

                        for k in newMarks:
                                while True:
                                        try:
                                                math = input(f"{k}: {YELLOW}")
                                                print(f"{WHITE}", end="")

                                                math.replace(" ","")

                                                marksList = list(map(float, math.split(",")))

                                                if len(marksList) == 6:
                                                        x = list(newMarks[k].keys())

                                                        # print()

                                                        for j in newMarks[k]:
                                                                newMarks[k][j] = marksList[x.index(j)]
                                                                # print(f"{j} {RED}:{WHITE} {YELLOW}{newMarks[k][j]}{WHITE}")
                                                        
                                                        # print()

                                                        break
                                                else:
                                                        print("Invalid Input")
                                        except ValueError or EOFError:
                                                print("Invalid Input")

                for i in newMarks:
                        for j in newMarks[i]:
                                if newMarks[i][j] > 100 and newMarks[i][j] <= 999:
                                        newMarks[i][j] = newMarks[i][j]/10
                                elif newMarks[i][j] >= 1000:
                                        newMarks[i][j] = 100

                classData[f"stud{newStudNum}"] = {
                        "Roll_No": newStudNum,
                        "IsDeleted": "False",
                        "Name": studentName,
                        "Subjects": newMarks
                }

                with open("gradesJSON/"+jsonFileName, "w") as existingData:
                        json.dump(classData, existingData, indent = 8)

                print("\n")
                printSpecificStudent(jsonFileName, newStudNum)




        elif grade >= 4 and grade <= 8:
                while True:
                        studentName = input(f"Enter Student's Name: {YELLOW}")
                        print(f"{WHITE}", end="")

                        if len(studentName) >= 1:
                                break
                        else:
                                print("Invalid Input")

                classData = loadJson(jsonFileName)
                newStudNum = len(classData) + 1

                print("\nDo you want to populate student's marks?")
                print("All marks will be set to 0 by default, if chosen 'NO', or left blank\n")
                
                try:
                        populateMarksBool = input(f"Enter 'Y' for YES and 'N' for NO {RED}(Other values will be considered 'NO'): {YELLOW}")
                        print(f"{WHITE}", end="")
                except populateMarksBool.lower() != "y" or populateMarksBool.lower() != "n" or EOFError:
                        populateMarksBool = "n"

                newMarks = {
                        "Math": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Science": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "SST": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Lang1": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Lang2": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Lang3": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "Computer": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                        "GK": {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 },
                }

                if populateMarksBool.lower() != "y" :
                        if populateMarksBool != "n":
                                print(f"{DEL_LINE}Enter 'Y' for YES and 'N' for NO "
                                f"{RED}(Other values will be considered 'NO')"
                                f": {YELLOW}*UNSUPPORTED VALUE*{WHITE}")
                        print("\nThank you! Marks for all subjects for all assessments has been set of zero."
                        " You can edit them later!")
                else:
                        print("\nEnter the marks in the order: ")
                        print(f"\n\t{YELLOW}[FA1, FA2, SA1, FA3, FA4, SA2]{WHITE}\n")
                        print("Enter them in comma seperated values. [Eg: 100, 88, 95, 79, 81]")

                        print(f"\nAny value greater than {YELLOW}100{WHITE} and less than {YELLOW}999{WHITE} will be made one tenth (Eg: {YELLOW}885{WHITE} will be converted to {YELLOW}88.5{WHITE})")
                        print(f"Any value greater than {YELLOW}1000{WHITE} will be considered {YELLOW}100{WHITE}\n")

                        print(f"{RED}Arbitrary values will throw you back to the input\n{WHITE}")

                        for k in newMarks:
                                while True:
                                        try:
                                                math = input(f"{k}: {YELLOW}")
                                                print(f"{WHITE}", end="")

                                                math.replace(" ","")

                                                marksList = list(map(float, math.split(",")))

                                                if len(marksList) == 6:
                                                        x = list(newMarks[k].keys())

                                                        # print()

                                                        for j in newMarks[k]:
                                                                newMarks[k][j] = marksList[x.index(j)]
                                                                # print(f"{j} {RED}:{WHITE} {YELLOW}{newMarks[k][j]}{WHITE}")
                                                        
                                                        # print()

                                                        break
                                                else:
                                                        print("Invalid Input")
                                        except ValueError or EOFError:
                                                print("Invalid Input")

                for i in newMarks:
                        for j in newMarks[i]:
                                if newMarks[i][j] > 100 and newMarks[i][j] <= 999:
                                        newMarks[i][j] = newMarks[i][j]/10
                                elif newMarks[i][j] >= 1000:
                                        newMarks[i][j] = 100

                classData[f"stud{newStudNum}"] = {
                        "Roll_No": newStudNum,
                        "IsDeleted": "False",
                        "Name": studentName,
                        "Subjects": newMarks
                }

                with open("gradesJSON/"+jsonFileName, "w") as existingData:
                        json.dump(classData, existingData, indent = 8)

                print("\n")
                printSpecificStudent(jsonFileName, newStudNum)




        elif grade == 9 or grade == 10:
                while True:
                        studentName = input(f"Enter Student's Name: {YELLOW}")
                        print(f"{WHITE}", end="")

                        if len(studentName) >= 1:
                                break
                        else:
                                print("Invalid Input")

                classData = loadJson(jsonFileName)
                newStudNum = len(classData) + 1

                optionalIndianLanguage = ["ASSAMESE", "BENGALI", "BHOTI", "BHUTIA", "BODO", "GUJARATI", "HINDI CORE", "HINDI ELECTIVE",
                                        "KANNADA", "KASHMIRI", "KOKBOROK", "LEPCHA", "LIMBOO", "MALAYALAM", "MANIPURI", "MARATHI", "MIZO",
                                        "NEPALI", "ODIA", "PUNJABI", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "SINDHI", "TAMIL", "TANGKHUL",
                                        "TELUGU AP", "TELUGU TELANGANA", "TIBETAN", "URDU CORE", "URDU ELECTIVE"]
                
                otherLanguageOptions = ["ARABIC", "FRENCH", "GERMAN", "ENGLISH CORE", "ENGLISH ELECTIVE", "JAPANESE", "PERSIAN", "RUSSIAN",
                                        "SPANISH", "ASSAMESE", "BENGALI", "BHOTI", "BHUTIA", "BODO", "GUJARATI", "HINDI CORE", "HINDI ELECTIVE",
                                        "KANNADA", "KASHMIRI", "KOKBOROK", "LEPCHA", "LIMBOO", "MALAYALAM", "MANIPURI", "MARATHI", "MIZO",
                                        "NEPALI", "ODIA", "PUNJABI", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "SINDHI", "TAMIL", "TANGKHUL",
                                        "TELUGU AP", "TELUGU TELANGANA", "TIBETAN", "URDU CORE", "URDU ELECTIVE"]
                
                otherElectives = ["CARNATIC MUSIC (VOCAL)", "CARNATIC MUSIC (MELODIC INSTRUMENTS)", "CARNATIC MUSIC (PERCUSSION INSTRUMENTS)",
                                "HINDUSTANI MUSIC (VOCAL)", "HINDUSTANI MUSIC (MELODIC INSTRUMENTS)", "HINDUSTANI MUSIC (PERCUSSION INSTRUMENTS)",
                                "PAINTING", "HOME SCIENCE", "NATIONAL CADET CORPS", "COMPUTER APPLICATIONS", "ELEMENTS OF BUSINESS",
                                "ELEMENTS OF BOOK KEEPING AND ACCOUNTANCY"]


                assessmentDict = {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 }

                newMarks = {
                        "MATH": assessmentDict,
                        "SCIENCE": assessmentDict,
                        "SST": assessmentDict
                }

                print("\nINDIAN LANGUAGE CHOICES\n-----------------------\033[3m")
                optedSubjects = selectSubs9and10(optionalIndianLanguage)

                for i in optedSubjects:
                        otherLanguageOptions.remove(i)

                print("\nOTHER LANGUAGE CHOICES\n----------------------\033[3m")
                optedSubjects.extend(selectSubs9and10(otherLanguageOptions))

                print("\nOTHER ELECTIVES\n---------------\033[3m")
                optedSubjects.extend(selectSubs9and10(otherElectives))

                for i in optedSubjects:
                        newMarks[i] = assessmentDict

                print("\nDo you want to populate student's marks?")
                print("All marks will be set to 0 by default, if chosen 'NO', or left blank\n")
                
                try:
                        populateMarksBool = input(f"Enter 'Y' for YES and 'N' for NO {RED}(Other values will be considered 'NO'): {YELLOW}")
                        print(f"{WHITE}", end="")
                except populateMarksBool.lower() != "y" or populateMarksBool.lower() != "n" or EOFError:
                        populateMarksBool = "n"

                print("\n\nSelect one or more subjects from the above list")

                if populateMarksBool.lower() != "y" :
                        if populateMarksBool != "n":
                                print(f"{DEL_LINE}Enter 'Y' for YES and 'N' for NO "
                                f"{RED}(Other values will be considered 'NO')"
                                f": {YELLOW}*UNSUPPORTED VALUE*{WHITE}")
                        print("\nThank you! Marks for all subjects for all assessments has been set of zero."
                        " You can edit them later!")
                else:
                        print("\nEnter the marks in the order: ")
                        print(f"\n\t{YELLOW}[FA1, FA2, SA1, FA3, FA4, SA2]{WHITE}\n")
                        print("Enter them in comma seperated values. [Eg: 100, 88, 95, 79, 81]")

                        print(f"\nAny value greater than {YELLOW}100{WHITE} and less than {YELLOW}999{WHITE} will be made one tenth (Eg: {YELLOW}885{WHITE} will be converted to {YELLOW}88.5{WHITE})")
                        print(f"Any value greater than {YELLOW}1000{WHITE} will be considered {YELLOW}100{WHITE}\n")

                        print(f"{RED}Arbitrary values will throw you back to the input\n{WHITE}")

                        for k in newMarks:
                                while True:
                                        try:
                                                math = input(f"{k}: {YELLOW}")
                                                print(f"{WHITE}", end="")

                                                math.replace(" ","")

                                                marksList = list(map(float, math.split(",")))

                                                if len(marksList) == 6:
                                                        x = list(newMarks[k].keys())

                                                        for j in newMarks[k]:
                                                                newMarks[k][j] = marksList[x.index(j)]                                                

                                                        break
                                                else:
                                                        print("Invalid Input")
                                        except ValueError or EOFError:
                                                print("Invalid Input")

                for i in newMarks:
                        for j in newMarks[i]:
                                if newMarks[i][j] > 100 and newMarks[i][j] <= 999:
                                        newMarks[i][j] = newMarks[i][j]/10
                                elif newMarks[i][j] >= 1000:
                                        newMarks[i][j] = 100

                classData[f"stud{newStudNum}"] = {
                        "Roll_No": newStudNum,
                        "IsDeleted": "False",
                        "Name": studentName,
                        "Subjects": newMarks
                }

                with open("gradesJSON/"+jsonFileName, "w") as existingData:
                        json.dump(classData, existingData, indent = 8)

                print("\n")
                printSpecificStudent(jsonFileName, newStudNum)




        elif grade == 11 or grade == 12:
                while True:
                        studentName = input(f"Enter Student's Name: {YELLOW}")
                        print(f"{WHITE}", end="")

                        if len(studentName) >= 1:
                                break
                        else:
                                print("Invalid Input")

                classData = loadJson(jsonFileName)
                newStudNum = len(classData) + 1

                optionalIndianLanguage = ["ASSAMESE", "BENGALI", "BHOTI", "BHUTIA", "BODO", "GUJARATI", "HINDI CORE", "HINDI ELECTIVE",
                                        "KANNADA", "KASHMIRI", "KOKBOROK", "LEPCHA", "LIMBOO", "MALAYALAM", "MANIPURI", "MARATHI", "MIZO",
                                        "NEPALI", "ODIA", "PUNJABI", "SANSKRIT CORE", "SANSKRIT ELECTIVE", "SINDHI", "TAMIL", "TANGKHUL",
                                        "TELUGU AP", "TELUGU TELANGANA", "TIBETAN", "URDU CORE", "URDU ELECTIVE"]
                
                otherLanguageOptions = ["ARABIC", "FRENCH", "GERMAN", "ENGLISH CORE", "ENGLISH ELECTIVE", "JAPANESE", "PERSIAN", "RUSSIAN",
                                        "SPANISH"]
                
                otherElectives = ["ACCOUNTANCY", "BIOLOGY", "BIO TECHNOLOGY", "BUSINESS STUDIES", "CARNATIC MELODIC", "CARNATIC VOCAL",
                                "CARNATIC PERCUSSION", "CHEMISTRY", "COMPUTER SCIENCE", "ECONOMICS", "ENGINEERING GRAPHICS", "ENTREPRENEURSHIP",
                                "FINE ARTS", "DANCE", "GEOGRAPHY", "HINDUSTANI MELODIC", "HINDUSTANI PERCUSSION", "HINDUSTANI VOCAL", "HISTORY",
                                "HOME SCIENCE", "INFORMATICS PRACTICES", "KNOWLEDGE TRADITION", "LEGAL STUDIES", "MATHEMATICS",
                                "APPLIED MATHEMATICS", "NCC", "PHYSICAL EDUCATION", "PHYSICS", "POLITICAL SCIENCE", "PSYCHOLOGY", "SOCIOLOGY"]

                assessmentDict = {"FA 1": 0, "FA 2": 0, "SA 1": 0, "FA 3": 0, "FA 4": 0, "SA 2": 0 }

                optedSubjects = []
                newMarks = {}

                indianLangCount = 0
                otherLangCount = 0

                print("\nLANGUAGE CHOICES\n----------------------\033[3m")
                selectSubs11and12(optionalIndianLanguage + otherLanguageOptions)

                print("\nOTHER ELECTIVES\n---------------\033[3m")
                selectSubs11and12(otherElectives)

                print(f"{YELLOW}Choose at least 5 and at most 12 subjects\n{WHITE}")

                while True:
                        subject = input(f"Enter your subject (Re-enter a subject to remove it from the list. Type QUIT to quit): {YELLOW}")
                        print(WHITE, end="")

                        subject = subject.upper()
                        subject = " ".join(subject.split())

                        if subject.lower() != 'quit':
                                if subject in optionalIndianLanguage or subject in otherLanguageOptions or subject in otherElectives:
                                        if subject not in optedSubjects:
                                                optedSubjects.append(subject)                                                
                                                print(f"{lb}\033[3mSubject added\n{WHITE}\033[0m")
                                        else:
                                                optedSubjects.remove(subject)

                                                if subject in optionalIndianLanguage:
                                                        indianLangCount -= 1
                                                elif subject in otherLanguageOptions:
                                                        otherLangCount -= 1

                                                print(f"{lb}\033[3mSubject removed\n{WHITE}\033[0m")
                                elif not subject.strip():
                                        print(f"{DEL_LINE}Enter your subject (Re-enter a subject to remove it from the list. Type QUIT to quit): {YELLOW}\033[3m*BLANK*\033[0m")
                                        print("Empty input is not supported\n")
                                else:
                                        print(f"{YELLOW}{subject}{WHITE} is not available\n")
                        else:
                                if len(optedSubjects) >=5 and len(optedSubjects) <= 12:
                                        for i in optedSubjects:
                                                if i in optionalIndianLanguage:
                                                        indianLangCount += 1

                                                if i in otherLanguageOptions:
                                                        otherLangCount += 1

                                        if indianLangCount + otherLangCount >= 2:
                                                if indianLangCount < 1 and otherLangCount >= 1:
                                                        print(f"{lb}\033[3mChoose at least one Indian XYZ language\n{WHITE}\033[0m")
                                                elif indianLangCount < 1 and otherLangCount < 1:
                                                        print(f"{lb}\033[3mChoose at least 2 languages, with at least one being an Indian language\n{WHITE}\033[0m")
                                                else:
                                                        break
                                        else:
                                                if indianLangCount < 1 and otherLangCount >= 1:
                                                        print(f"{lb}\033[3mChoose at least one Indian language\n{WHITE}\033[0m")
                                                elif indianLangCount < 1 and otherLangCount < 1:
                                                        print(f"{lb}\033[3mChoose at least 2 languages, with at least one being an Indian language\n{WHITE}\033[0m")
                                                else:
                                                        print(f"{lb}\033[3mChoose one more language subject\n{WHITE}\033[0m")
                                elif len(optedSubjects) < 5:
                                        print(f"{lb}\033[3mChoose 5 subjects at least (Has chosen {len(optedSubjects)} yet)\n{WHITE}\033[0m")
                                else:
                                        print(f"{lb}\033[3mChoose 12 subjects at most (Has chosen {len(optedSubjects)})\n{WHITE}\033[0m")

                for i in optedSubjects:
                        newMarks[i] = assessmentDict

                print("\nDo you want to populate student's marks?")
                print("All marks will be set to 0 by default, if chosen 'NO', or left blank\n")

                try:
                        populateMarksBool = input(f"Enter 'Y' for YES and 'N' for NO {RED}(Other values will be considered 'NO'): {YELLOW}")
                        print(f"{WHITE}", end="")
                except populateMarksBool.lower() != "y" or populateMarksBool.lower() != "n" or EOFError:
                        populateMarksBool = "n"

                print("\n\nSelect one or more subjects from the above list")

                if populateMarksBool.lower() != "y" :
                        if populateMarksBool != "n":
                                print(f"{DEL_LINE}Enter 'Y' for YES and 'N' for NO "
                                f"{RED}(Other values will be considered 'NO')"
                                f": {YELLOW}*UNSUPPORTED VALUE*{WHITE}")
                        print("\nThank you! Marks for all subjects for all assessments has been set of zero."
                        " You can edit them later!")
                else:
                        print("\nEnter the marks in the order: ")
                        print(f"\n\t{YELLOW}[FA1, FA2, SA1, FA3, FA4, SA2]{WHITE}\n")
                        print("Enter them in comma seperated values. [Eg: 100, 88, 95, 79, 81]")

                        print(f"\nAny value greater than {YELLOW}100{WHITE} and less than {YELLOW}999{WHITE} will be made one tenth (Eg: {YELLOW}885{WHITE} will be converted to {YELLOW}88.5{WHITE})")
                        print(f"Any value greater than {YELLOW}1000{WHITE} will be considered {YELLOW}100{WHITE}\n")

                        print(f"{RED}Arbitrary values will throw you back to the input\n{WHITE}")

                        for k in newMarks:
                                while True:
                                        try:
                                                math = input(f"{k}: {YELLOW}")
                                                print(f"{WHITE}", end="")

                                                math.replace(" ","")

                                                marksList = list(map(float, math.split(",")))

                                                if len(marksList) == 6:
                                                        x = list(newMarks[k].keys())

                                                        for j in newMarks[k]:
                                                                newMarks[k][j] = marksList[x.index(j)]                                                

                                                        break
                                                else:
                                                        print("Invalid Input")
                                        except ValueError or EOFError:
                                                print("Invalid Input")

                for i in newMarks:
                        for j in newMarks[i]:
                                if newMarks[i][j] > 100 and newMarks[i][j] <= 999:
                                        newMarks[i][j] = newMarks[i][j]/10
                                elif newMarks[i][j] >= 1000:
                                        newMarks[i][j] = 100

                classData[f"stud{newStudNum}"] = {
                        "Roll_No": newStudNum,
                        "IsDeleted": "False",
                        "Name": studentName,
                        "Subjects": newMarks
                }

                with open("gradesJSON/"+jsonFileName, "w") as existingData:
                        json.dump(classData, existingData, indent = 8)

                print("\n")
                printSpecificStudent(jsonFileName, newStudNum)




        else:
                print("Error")



