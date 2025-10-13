import pickle

d = {"stu1": {"Name": "John","Age": "21","ID":28},
"stu2": {"Name": "Bob","Age": "99","ID":28},
"stu3": {"Name": "Js","Age": "70","ID":28},
}

with open("students.dat", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("students.dat", "rb") as file2:
    mydictionary = pickle.load(file2)

print(mydictionary)
file2.close()

