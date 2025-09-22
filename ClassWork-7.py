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
                value = input("Please provide the value of the dictionary you want to update: ")

    elif option == "4":
        for project_record in Projects.items():
            print(project_record)
            print("------------------------------------")

    elif option == "5":
        break

print("Thank you for using this program!")



