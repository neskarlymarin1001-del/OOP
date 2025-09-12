print("Welcome!")

stu_name = []
stu_age  = []
while True:
    print("Please choose one of the following: ")
    print("1. Add an element to the list")
    print("2. Remove a specific element from the list")
    print("3. Replace an element in the list")
    print("4. Print the list elements")
    print("5. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        newName = input("Please provide the name of the student you want to add: ")
        stu_name.append(newName)
        newAge = input("Please provide the age of the student you want to add: ")
        stu_age.append(newAge)

    elif option == "2":
        if len(stu_name) == 0:
            print("The list is empty")
        else:
            oldStudent = input("Please provide the name of the student you want to remove: ")
            if oldStudent not in stu_name:
                print("That student is not in the list")
            else:
                stu_name.remove(oldStudent)

    elif option == "3":
        x = (int(input("What is the index of the student to be replaced? ")))
        if x < len(stu_name):
            newStudent = input("Please provide the new name you want to add: ")
            stu_name[x] = newStudent
            newStudentAge = input("Please provide the student's age you want to add: ")
            stu_age[x] = newStudentAge
        else:
            print("There is not an element in that index")


    elif option == "4":
        print(stu_name)
        print(stu_age)

    elif option == "5":
        break

print("Thank you for using this program!")