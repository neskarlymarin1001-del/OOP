print("Welcome!")

myStudents = {}

while True:
    print("Please choose one of the following: ")
    print("1. Add a record to the dictionary")
    print("2. Delete a record from the dictionary")
    print("3. Replace a record in the dictionary")
    print("4. Print the dictionary")
    print("5. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        sid = input("Please provide the student's ID: ")
        nname = input("Please provide the student's name: ")
        mmajor = input("Please provide the student's major: ")
        yyear = input("Please provide the student's year: ")
        ttc = int(input("Please provide the student's total credits: "))
        ggpa = float(input("Please provide the student's GPA: "))

        myStudents.update({sid:{
                                    "name":nname,
                                    "major":mmajor,
                                    "year":yyear,
                                    "tc":ttc,
                                    "gpa":ggpa
                                 }
                               })
    elif option == "2":
        if len(myStudents) == 0:
            print("The dictionary is empty")
        else:
            oldStudent = input("Please provide the ID of the student you want to remove: ")
            if oldStudent not in myStudents:
                print("That student is not in the dictionary")
            else:
                del myStudents[oldStudent]

    elif option == "3":
        if len(myStudents) == 0:
            print("The dictionary is empty")
        else:
            oldStudent = input("Please provide the ID of the student you want to replace: ")
            if oldStudent not in myStudents:
                print("That student is not in the list")
            else:
                newStudent = input("Please provide the new ID you want to add: ")
                myStudents[oldStudent]=newStudent

    elif option == "4":
        for student_record in myStudents.items():
             print(student_record)
             print("------------------------------------")

    elif option == "5":
        break

    print("Thank you for using this program!")

