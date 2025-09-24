def area_rectangle():
    l = int(input("Enter length"))
    b = int(input("Enter breadth"))
    print("The are of the rectangle is:", l*b)

def volume_cube():
    l = int(input("Enter the length"))
    b = int(input("Enter breadth"))
    h = int(input("Enter height"))
    print("The volume of the cube is:", l*b*h)

def area_circle():
    r = int(input("Enter radius"))
    print("The are of the circle is:", 3.14*r*r)

def circumference_circle():
    r = int(input("Enter radius"))
    print("The circumference of the circle is:", 2*3.14*r)

def volume_sphere():
    r = int(input("Enter radius"))
    print("The volume of the sphere is:", (4/3)*3.14*r*r*r)

print("Welcome to the area calculator!")

while True:
    print("Please choose one of the following: ")
    print("1. Calculate area of a rectangle")
    print("2. Calculate volume of a cube")
    print("3. Calculate area of a circle")
    print("4. Circumference of a circle")
    print("5. Calculate the volume of a sphere")
    print("6. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        area_rectangle()

    if option == "2":
        volume_cube()

    if option == "3":
        area_circle()

    if option == "4":
        circumference_circle()

    if option == "5":
        volume_sphere()

    if option == "6":
        break

print("Thank your for using this program!")

