import json

def registerStudent(data):
    loopName = 0
    while loopName == 0:
        name = ""
        while name == "":
            name = input("\nEnter the student's name: ").strip().lower()
            if name == "":
                print("You cannot leave this blank!")
            else:
                loopName = 1
    
    loopStudentID = 0
    while loopStudentID == 0:
        studentID = ""
        while studentID == "" or len(studentID) != 10:
            studentID = input("\nEnter the student's ID number (10 numbers): ").strip().replace(" ", "")
            if studentID in data.keys():
                print("This student ID is already registered, try again.")
                studentID = ""      
            elif len(studentID) != 10:
                print("Student ID is not valid")
            elif studentID == "":
                print("You cannot leave this blank")
            else:
                loopStudentID = 1
    
    loopAge = 0
    while loopAge == 0:
        age = ""
        while age == "" or int(age) <= 0 or len(age) > 2:
            try:
                age = input("\nEnter the student's age: ").strip().replace(" ", "")
            except ValueError:
                print("Please enter a valid student age number")
            if age == "" or int(age) <= 0 or len(age) > 2:
                print("Please enter valid student age number")
            else:
                loopAge = 1
    
    loopStudentClass = 0
    while loopStudentClass == 0:
        studentClass = ""
        while studentClass == "":
            studentClass = input("\nEnter the student's class: ").strip().lower()
            if studentClass == "":
                print("You cannot leave this blank!")
            else:
                loopStudentClass = 1
    
    loopActive = 0
    while loopActive == 0:
        isActive = ""
        while isActive == "":
            isActive = input("\nIs the student currently active? (Yes/No): ").strip().lower()
            if isActive == "yes" or isActive == "y":
                isActive = True
                loopActive = 1
            elif isActive == "no" or isActive == "n":
                isActive = False
                loopActive = 1
            else: 
                print("Please enter a valid option")
                isActive = ""
    
    studentData = {"name":name,"age":age,"class":studentClass,"is active?":isActive}
    data[studentID] = studentData
    return data

def showList(data):
    for i, (studentID, things) in enumerate(data.items(), start=1):
        print(f"\n-{i}: \nStudent ID: {studentID}\nName: {things["name"]}\nAge: {things["age"]}\nClass: {things["class"]}\nActive: {things["is active?"]}")
    
def searchStudentByName(data):
    nameloop = 0
    while nameloop == 0:
        name = ""
        while name == "":
            name = input("Please enter the student's name: ").strip().lower()
            if name == "":
                print("You can not leave this blank")
            else:
                nameloop = 1
    for student in data.values():
        if student["name"] == name:
            print("The student is registered")
            break
    else:
        print("The student is not registered")

def searchStudentByID(data):
    studIDloop = 0
    while studIDloop == 0:
        studID = ""
        while studID == "":
            studID = input("ID: ").strip()
            if studID == "":
                print("You can not leave this blank")
            else:
                studIDloop = 1
    if studID in data:
        print("The student is registered")
    else:
        print("The student is not registered")

def updateStudent(data):
    studloop = 0
    while studloop == 0:
        studID = ""
        while studID == "":
            studID = input("Please enter the student ID number: ").strip()
            if studID == "":
                print("You can not leave this blank")
            else:
                studloop = 1
    if studID in data:
        isactiveloop = 0
        while isactiveloop == 0:
            isactive = ""
            while isactive == "":
                isactive = input("Is the student currently active? (Yes/No): ").strip().lower()
                if isactive == "":
                    print("You cannot leave this blank")
            if isactive == "yes" or isactive == "y":
                isActive = True
                isactiveloop = 1
            elif isactive == "no" or isactive == "n":
                isActive = False
                isactiveloop = 1
            else:
                print("Enter a valid option")
        data[studID]["is active?"] = isActive
        
def deleteInfo(data):
    deleteloop = 0
    while deleteloop == 0:
        studID = ""
        while studID == "":
            studID = input("Please enter the student ID number you want to delete from the list: ").strip()
            if studID == "":
                print("You cannot leave this blank")
        if studID in data:
            choice = ""
            while choice == "":
                choice = input(f"Are you sure you want to delete {data[studID]["name"].title()} data? (Yes/No): ").strip().lower()
                if choice == "":
                    print("You cannot leave this blank")
            if choice == "yes" or choice == "y":
                print(f"Deleting data...")
                data.pop(studID)
                deleteloop = 1
        else:
            print("User not registered")

def saveData(dataName, data):
    if not dataName:
        loopdata = 0
        while loopdata == 0:
            dataName = ""
            while dataName == "":
                dataName = input("Input the file name: ")
                if not dataName.endswith(".json"):
                    print("Invalid JSON file")
                    dataName = ""
        with open(dataName, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    else:
        with open(dataName, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    return dataName, data

def loadData(dataName, data):
    dataName = input("Input the file name: ")
    if not dataName.endswith(".json"):
        print("Invalid JSON file")
        dataName = False
    else:
        try:
            with open(dataName, 'r',encoding='utf-8') as f:
                    data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error de formato JSON: {e}")
        except FileNotFoundError:
            print(f"Error: El archivo {dataName} no existe.\n")
            data = {}
            dataName = False
    return dataName, data


options = {
    "menu":{
        "1": "register",
        "register":"register",
        "2":"show",
        "show":"show",
        "list":"show",
        "3":"search",
        "search":"search",
        "4":"update",
        "update":"update",
        "5":"delete",
        "delete":"delete",
        "6":"save",
        "save":"save",
        "7":"load",
        "load":"load",
        "8":"exit",
        "exit":"exit"
    }
}
data = {

}

dataName = False

loopMenu = 0
while loopMenu == 0:
    if not dataName:
        print("\n!-- You are not inside a file")
    else:
        print(f"\n!-- Inside '{dataName}' file")
    menuOption = input("\nPlease select an option:\n1.Register a new student\n2.Show student list\n3.Search student by name or ID\n4.Update student info\n5.Delete student info\n6.Save student data\n7.Load student data\n8.Close\n--- ")
    if menuOption in options["menu"]:
        menuOption = options["menu"][menuOption]
        if menuOption == "register":
            data = registerStudent(data)
        elif menuOption == "show":
            showList(data)
        elif menuOption == "search":
            searchOption = input("Search by name or ID: ")
            if searchOption == "name":
                searchStudentByName(data)
            elif searchOption == "id":
                searchStudentByID(data)
        elif menuOption == "update":
            updateStudent(data)
        elif menuOption == "delete":
            deleteInfo(data)
        elif menuOption == "save":
            dataName, data = saveData(dataName, data)
        elif menuOption == "load":
            dataName, data = loadData(dataName, data)
        elif menuOption == "exit":
            print("Closing...")
            loopMenu = 1
    else:
        print("Enter a valid option.")