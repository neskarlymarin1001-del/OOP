import pickle

with open("students.dat", "rb") as file2:
    mydictionary = pickle.load(file2)

file2.close()

print(mydictionary["stu1"]["Name"],mydictionary["stu1"]["Age"])

i=1
for x in mydictionary:
    var = "stu"+str(i)
    print(mydictionary[var]["Name"])
    i+=1