print("Welcome!")

myEmployees = {}

while True:
    print("Please choose one of the following: ")
    print("1. Add a record to the dictionary")
    print("2. Delete a record from the dictionary")
    print("3. Replace a record in the dictionary")
    print("4. Print the dictionary")
    print("5. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        idd = input("Please provide the employees's ID: ")
        nname = input("Please provide the employees's name: ")
        bbasicPay = float(input("Please provide the employees's basic pay: "))
        aallowance = float(input("Please provide the employees's allowance: "))
        ddeductions = float(input("Please provide the employees's deductions: "))
        ttaxes = float(input("Please provide the employees's taxes: "))
        nnetPay = bbasicPay + aallowance
        ggrossPay = nnetPay - ddeductions - ttaxes

        myEmployees.update({idd:{
                                    "Name":nname,
                                    "BasicPay":bbasicPay,
                                    "Allowance":aallowance,
                                    "Deductions":ddeductions,
                                    "Taxes":ttaxes,
                                    "NetPay":nnetPay,
                                    "GrossPay":ggrossPay
                                 }
                               })
    elif option == "2":
        if len(myEmployees) == 0:
            print("The dictionary is empty")
        else:
            oldEmployee = input("Please provide the ID employee you want to remove: ")
            if oldEmployee not in myEmployees:
                print("That employee is not in the dictionary")
            else:
                del myEmployees[oldEmployee]

    elif option == "3":
        if len(myEmployees) == 0:
            print("The dictionary is empty")
        else:
            oldEmployee = input("Please provide the ID of the employee you want to modify: ")
            if oldEmployee not in myEmployees:
                print("That employee is not in the list")
            else:
                nname = input("Please provide the employees's name: ")
                bbasicPay = float(input("Please provide the employees's basic pay: "))
                aallowance = float(input("Please provide the employees's allowance: "))
                ddeductions = float(input("Please provide the employees's deductions: "))
                ttaxes = float(input("Please provide the employees's taxes: "))
                nnetPay = bbasicPay + aallowance
                ggrossPay = nnetPay - ddeductions - ttaxes

                myEmployees[oldEmployee].update({
                    "Name": nname,
                    "BasicPay": bbasicPay,
                    "Allowance": aallowance,
                    "Deductions": ddeductions,
                    "Taxes": ttaxes,
                    "NetPay": nnetPay,
                    "GrossPay": ggrossPay
                })


    elif option == "4":
        for employee_record in myEmployees.items():
             print(employee_record)
             print("------------------------------------")

    elif option == "5":
        print("Thank you for using this program!")
        break

   



