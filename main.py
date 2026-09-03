students = []

def load_students():
    try:
        with open("students.txt",'r') as file:
            lines = file.read().split("\n")
        for line in lines:
            data = line.split(" | ")
            if(len(data)==5):
                student = {
                    "regno"  : int(data[0]),
                    "name"    : data[1],
                    "age"     : int(data[2]),
                    "program" : data[3],
                    "cgpa"    : float(data[4])
                }
                students.append(student)
    except FileNotFoundError:
        pass


    
def regno_exist(regno):
    for student in students:
        if(regno == student["regno"]):
            return True
    return False



def add_student():
    print("Enter Student Details:-")
    while True:
        try:
            regno = int(input("Register Number: "))
        except ValueError:
            print("Register Number Should Be A Whole Number.\n")
            continue
        if(not(regno_exist(regno))):
            break
        print(f"Register No. {regno} is Assign Someone Else\n")

    name = input("Name: ")
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Age Should Be A Whole Number.\n")
    program = input("Program: ")
    try:
        cgpa = float(input("CGPA: "))
    except ValueError:
        print("CGPA Cantains Only Digit.\n")
    
    student = {
        "regno"  : regno,
        "name"    : name,
        "age"     : age,
        "program" : program,
        "cgpa"    : cgpa
    }
    students.append(student)
    with open("students.txt",'a') as file:
        file.write(f"{regno} | {name} | {age} | {program} | {cgpa}\n")
    return True

def view_students():
    if(len(students)==0):
        print("'NO STUDENT RECORDS'")
        return
    count = 1
    for student in students:
        print("-----------------------------------")
        print(f"Student({count}) Details:-")
        print(f"Registration Number :  {student['regno']}")
        print(f"Name                :  {student['name']}")
        print(f"Age                 :  {student['age']}")
        print(f"Program             :  {student['program']}")
        print(f"CGPA                :  {student['cgpa']}")
        print("-----------------------------------")
        count+=1

def search_student():
    if(len(students)==0):
        print("'NO STUDENT RECORDS'")
        return
    while True:
            try:
                regno = int(input("Enter Register Number: "))
            except ValueError:
                print("Register Number Should Be A Whole Number.\n")
                continue
            if(regno_exist(regno)):
                break
            print(f"Register No. {regno} is Not Assign Anyone\n")
    for student in students:
        if student["regno"] == regno:
            print("\n-----------------------------------")
            print(f"Student Details:-")
            print(f"Registration Number :  {student['regno']}")
            print(f"Name                :  {student['name']}")
            print(f"Age                 :  {student['age']}")
            print(f"Program             :  {student['program']}")
            print(f"CGPA                :  {student['cgpa']}")
            print("-----------------------------------")
            break

def reWriteFile():
    with open("students.txt",'w') as file:
        for student in students:
            file.write(f"{student['regno']} | {student['name']} | {student['age']} | {student['program']} | {student['cgpa']}\n")
        


def update_student():
    if(len(students)==0):
        print("'NO STUDENT RECORDS'")
        return
    while True:
            try:
                regno = int(input("Enter Register Number: "))
            except ValueError:
                print("Register Number Should Be A Whole Number.\n")
                continue
            if(regno_exist(regno)):
                break
            print(f"Register No. {regno} is Not Assign Anyone\n")

    for student in students:
        if(student["regno"] == regno):
            while True:
                print("\n========= Update Window =========")
                print("1) Update Name")
                print("2) Update Age")
                print("3) Update Program")
                print("4) Update CGPA")
                print("5) Exit")
                print("===================================")
                try:
                    opt = int(input("Enter Option Number: "))
                except ValueError:
                    print("'INVALID OPTION NUMBER'")
                    enter = input("\nPRESS ENTER TO CONTINUE...")
                    continue

                if(opt == 1):
                    print(f"\nCurrent Name : {student['name']}")
                    student['name'] = input("New Name     : ")
                    print("'SUCCESSFULLY UPDATE'")
                elif(opt == 2):
                    print(f"\nCurrent Age : {student['age']}")
                    student['age'] = int(input("New Age     : "))
                    print("'SUCCESSFULLY UPDATE'")
                elif(opt == 3):
                    print(f"\nCurrent Program : {student['program']}")
                    student['program'] = input("New Program     : ")
                    print("'SUCCESSFULLY UPDATE'")
                elif(opt == 4):
                    print(f"\nCurrent CGPA : {student['cgpa']}")
                    student['cgpa'] = float(input("New CGPA     : "))
                    print("'SUCCESSFULLY UPDATE'")
                elif(opt == 5):
                    print("\n'EXIT SUCCESSFUL'")
                    break
                else:
                    print("'INVALID OPTION NUMBER'")
                    enter = input("\nPRESS ENTER TO CONTINUE...")
            break 
    reWriteFile()    

            

def delete_student():
    if(len(students)==0):
        print("'NO STUDENT RECORDS'")
        return
    while True:
            try:
                regno = int(input("Enter Register Number: "))
            except ValueError:
                print("Register Number Should Be A Whole Number.\n")
                continue
            if(regno_exist(regno)):
                break
            print(f"Register No. {regno} is Not Assign Anyone\n")
    conferme = input("Are you Sure? (yes/no): ").lower()
    if(conferme == "yes"):
        for student in students:
            if(student['regno']==regno):
                students.remove(student)
                reWriteFile()
                print("'STUDENT DELETED'")
                break
    else:
        print("'ACTION TERMINATED'")
        return
    

#----------------------------------------------------------------------------------
print("\n-----------------------------------")
print("|    STUDENT MENEGEMENT SYSTEM    |")
print("-----------------------------------")

load_students()

while True:
    print("\n============== MENU ===============")
    print("1) Add Student")
    print("2) View All Students")
    print("3) Search Student")
    print("4) Update Student Record")
    print("5) Delete Student Record")
    print("6) Exit")
    print("===================================")

    try:
        opt = int(input("Enter Option Number: "))
    except:
        print("-----------------------------------")
        print("       INVALID OPTION NUMBER       ")
        print("-----------------------------------")
        enter = input("\nPRESS ENTER TO CONTINUE...")
        continue       

    if(opt==1):
        print("-----------------------------------")
        print("            Add Student            ")
        print("-----------------------------------")
        if add_student():
            print("-----------------------------------")
            print("         Succesfully Added         ")
            print("-----------------------------------")
    elif(opt==2):
        print("-----------------------------------")
        print("           All Students            ")
        print("-----------------------------------")
        view_students()
    elif(opt==3):
        print("-----------------------------------")
        print("          Search Student           ")
        print("-----------------------------------")
        search_student()
    elif(opt==4):
        print("-----------------------------------")
        print("         Update Student            ")
        print("-----------------------------------")
        update_student()
    elif(opt==5):
        print("-----------------------------------")
        print("         Delete Student            ")
        print("-----------------------------------")
        delete_student()
    elif(opt==6):
        print("-----------------------------------")
        print("          EXIT SUCCESSFUL          ")
        print("-----------------------------------")
        break  

    else:
        print("-----------------------------------")
        print("       INVALID OPTION NUMBER       ")
        print("-----------------------------------")

    enter = input("\nPRESS ENTER TO CONTINUE...")