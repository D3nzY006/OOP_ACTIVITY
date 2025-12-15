class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def course(self):
        print(self.name, "is a Senior High School Student")

class Teacher(Person):
    def subject(self):
        print(self.name, "is a Math teacher")

student = Student("John")
student.course()

teacher = Teacher("Mark")
teacher.subject()