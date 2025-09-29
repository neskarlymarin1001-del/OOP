print("Welcome!")

myList = []
while True:
    print("Please choose one of the following: ")
    print("1. Add an element to the list")
    print("2. Remove a specific element from the list")
    print("3. Pop the last element")
    print("4. Display the list")
    print("5. Quit")

    option = input("Please enter your choice here: ")

    if option == "1":
        newElement = input("Please provide the element you want to add: ")
        myList.append(newElement)

    elif option == "2":
        if len(myList) == 0:
            print("The list is empty")
        else:
            print("These are the elements on the list: ")
            print(myList)
            oldElement = input("Please provide the element you want to remove: ")
            if oldElement not in myList:
                print("That element is not in the list")
            else:
                myList.remove(oldElement)

    elif option == "3":
        if len(myList) == 0:
            print("The list is empty")
        else:
            myList.pop()

    elif option == "4":
        print(myList)

    elif option == "5":
        break


