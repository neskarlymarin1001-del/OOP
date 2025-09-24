myQueue=[]

def Enqueue():
    new_value = input("Provide the element you want to add: ")
    myQueue.append(new_value)

def Dequeue():
    myQueue.remove(myQueue[0])


while 1:
    print("Please choose one of the following: ")
    print("1. Add a new element at the end")
    print("2. Remove the first element from the list")
    print("3. Print list")
    print("4. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        Enqueue()

    if option == "2":
        Dequeue()

    elif option == "3":
        print(myQueue)

    if option == "4":
        break

print("Thank you for using this program!")



