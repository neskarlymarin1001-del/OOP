from bdb import Breakpoint
print("Welcome to the best Calculator Program!")
while True:
    print("Please choose one of the following: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    option = input("Please enter your choice here: ")

    if option == "1":
        n1 =int(input("Please enter the first number: "))
        n2 = int(input("Please enter the second number: "))
        result = n1 + n2
        print("The sum of", n1, "and", n2, "is", result)

    if option == "2":
        n1 =int(input("Please enter the first number: "))
        n2 = int(input("Please enter the second number: "))
        result = n1 - n2
        print("The difference of", n1, "and", n2, "is", result)

    if option == "3":
        n1 =int(input("Please enter the first number: "))
        n2 = int(input("Please enter the second number: "))
        result = n1 * n2
        print("The product of", n1, "and", n2, "is", result)

    if option == "4":
        n1 =int(input("Please enter the first number: "))
        n2 = int(input("Please enter the second number: "))
        result = n1 / n2
        print("The division of", n1, "and", n2, "is", result)

    if option == "5":
        break

print("Thank you for using this Calculator Progam!")


