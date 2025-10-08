class Student:
    def __init__(self):
        self.SID = ""
        self.stu_Name = ""
        self.dob = ""
        self.major = ""
        self.gpa = 0.0
        self.courses = []

    def add_student(self):
        self.SID = input("Enter the SID: ")
        self.stu_Name = input("Enter the student name: ")
        self.dob = input("Enter the student dob: ")
        self.major = input("Enter the student major: ")
        self.gpa = input("Enter the student GPA: ")

    def edit_student(self):
        self.stu_Name = input("Enter the update Name for the student: ")
        self.gpa = input("Enter the update GPA for the student: ")

    def register_courses(self, cc1):
        self.courses.append(cc1)

    def display_student(self):
        print("StuID: ", self.SID)
        print("Stu Name: ", self.stu_Name)
        print("Stu dob: ", self.dob)
        print("Stu major: ", self.major)
        print("Stu GPA: ", self.gpa)
        for x in self.courses:
            print("Course: ", x.cname)

class Courses:
    def __init__(self):
        self.cid = ""
        self.cname = ""

    def add_course(self):
        self.cid = input("Enter the CID: ")
        self.cname = input("Enter the course name: ")

# Main Code

s1 = Student()
c1 = Courses()
c2 = Courses()

s1.add_student()

c1.add_course()
c2.add_course()

s1.register_courses(c1)
s1.register_courses(c2)

s1.display_student()



