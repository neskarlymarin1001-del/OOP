a = int (input("Enter the value of a: "))
b = int (input("Enter the value of b: "))
c = int (input("Enter the value of c: "))

if a > b and a > c:
    print ("A is greater")

elif b > a and b > c:
    print ("B is greater")

elif c > a and c > b:
    print ("C is greater")

else:
    print("They are equal")

