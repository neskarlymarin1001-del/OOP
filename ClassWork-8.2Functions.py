myStack=[]

def Stack():
    new_value = input("Provide the element you want to add: ")
    myStack.append(new_value)

def onStack():
    myStack.pop()


while 1:
    print("Please choose one of the following: ")
    print("1. Add a new element at the end")
    print("2. Remove the last element from the list")
    print("3. Print list")
    print("4. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        Stack()

    if option == "2":
        onStack()

    elif option == "3":
        print(myStack)

    if option == "4":
        break

print("Thank you for using this program!")



