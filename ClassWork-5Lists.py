print("Welcome!")

myList = []
while True:
    print("Please choose one of the following: ")
    print("1. Add an element to the list")
    print("2. Remove a specific element from the list")
    print("3. Replace an element in the list")
    print("4. Sort the elements in the list")
    print("5. Reverse the elements in the list")
    print("6. Print the list elements")
    print("7. Exit")

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
        x = (int(input("What is the index of the element to be replaced? ")))
        if x < len(myList):
            newElement = input("Please provide the new element you want to add: ")
            myList[x] = newElement
        else:
            print("There is not an element in that index")

    elif option == "4":
        myList.sort()

    elif option == "5":
        myList.reverse()

    elif option == "6":
        print(myList)

    elif option == "7":
        break

print("Thank you for using this program!")
