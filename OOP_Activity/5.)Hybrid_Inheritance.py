class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def role(self):
        print(self.name, "is a College student")

class Course(Person):
    def __init__(self, course_name):
        self.course__name = course_name

class ClassAdviser(Student, Course):
    def __init__(self, name, course_name):
        Student.__init__(self, name)     
        Course.__init__(self, course_name)
        

    def details(self):
        print(self.name, "is a", self.course__name)

cadviser = ClassAdviser("John", "Bachelor of Science in Information Systems")
cadviser.role()
cadviser.details()

