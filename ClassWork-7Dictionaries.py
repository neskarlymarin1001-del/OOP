print("Welcome!")

Projects = {}

while True:
    print("Please choose one of the following: ")
    print("1. Project Initiation")
    print("2. Project Closure")
    print("3. Project Progress Update")
    print("4. Print All Projects")
    print("5. Quit Application")

    option = input("Please enter your choice here: ")

    if option == "1":
        mmanagers = []
        ttechnologies = []
        teamMembers = []

        pid = input("Please provide the project's ID: ")
        projectTitle = input("Please provide the project's title: ")
        n = int(input("How many managers do you want to add? "))
        for i in range(0,n):
            mmanagers.append(input("Please provide the manager name you want to add: "))
        startDate = input("Please provide start date: ")
        endDate = input("Please provide end date: ")
        ssponsor = input("Please provide the sponsor: ")
        bbudget = float(input("Please provide the budget for the project: "))
        n = int(input("How many technologies do you want to add? "))
        for i in range(0, n):
            ttechnologies.append(input("Please provide the technology you want to add: "))
        n = int(input("How many team members do you want to add? "))
        for i in range(0, n):
            teamMembers.append(input("Please provide the team member name you want to add: "))

        Projects.update({pid:{
                                    "Project_Title":projectTitle,
                                    "Managers":mmanagers,
                                    "Start_Date":startDate,
                                    "End_Date":endDate,
                                    "Sponsors":ssponsor,
                                    "Budget": bbudget,
                                    "Technologies": ttechnologies,
                                    "Team_Members": teamMembers
                                 }
                               })

    elif option == "2":
        if len(Projects) == 0:
            print("The dictionary is empty")
        else:
            oldProject = input("Please the ID of the project you want to remove: ")
            if oldProject not in Projects:
                print("That project is not in the dictionary")
            else:
                del Projects[oldProject]

    elif option == "3":
    if len(Projects) == 0:
        print("The dictionary is empty")
    else:
        oldProject = input("Please provide the ID of the project you want to update: ")
        if oldProject not in Projects:
            print("That project is not in the dictionary")
        else:
            print("What would you like to update?")
            print("1. Project Title")
            print("2. Managers")
            print("3. Start Date")
            print("4. End Date")
            print("5. Sponsors")
            print("6. Budget")
            print("7. Technologies")
            print("8. Team Members")

            choice = input("Enter the number of the field you want to update: ")

            if choice == "1":
                new_value = input("Enter new Project Title: ")
                Projects[oldProject]["Project_Title"] = new_value

            elif choice == "2":
                new_list = []
                n = int(input("How many managers do you want to add? "))
                for i in range(n):
                    new_list.append(input("Enter manager name: "))
                Projects[oldProject]["Managers"] = new_list

            elif choice == "3":
                new_value = input("Enter new Start Date: ")
                Projects[oldProject]["Start_Date"] = new_value

            elif choice == "4":
                new_value = input("Enter new End Date: ")
                Projects[oldProject]["End_Date"] = new_value

            elif choice == "5":
                new_value = input("Enter new Sponsor: ")
                Projects[oldProject]["Sponsors"] = new_value

            elif choice == "6":
                new_value = float(input("Enter new Budget: "))
                Projects[oldProject]["Budget"] = new_value

            elif choice == "7":
                new_list = []
                n = int(input("How many technologies do you want to add? "))
                for i in range(n):
                    new_list.append(input("Enter technology: "))
                Projects[oldProject]["Technologies"] = new_list

            elif choice == "8":
                new_list = []
                n = int(input("How many team members do you want to add? "))
                for i in range(n):
                    new_list.append(input("Enter team member: "))
                Projects[oldProject]["Team_Members"] = new_list

            else:
                print("Invalid option")

    elif option == "4":
        for project_record in Projects.items():
            print(project_record)
            print("------------------------------------")

    elif option == "5":
        break

print("Thank you for using this program!")




