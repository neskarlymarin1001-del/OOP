file1 = open("test1.txt", "w")
file1.writelines("Hello World! \n")
file1.writelines("Welcome to the OOP Class!\n")
file1.writelines("I hope you're enjoying it!\n")

file1.close()

file2 = open("test1.txt", "r")

for line in file2:
    print(line)
file2.close()

