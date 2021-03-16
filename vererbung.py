class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return self.firstname + " " + self.lastname

class WorkingStudent(Student):
    def __init__(self, firstname, lastname, company):
        super().__init__(firstname, lastname)
        self.company = company


student = Student("Max", "Müller")

wStudent = WorkingStudent("Peter", "Lustig","Knaup & Co")
print(isinstance(wStudent, Student))
print(isinstance(student, WorkingStudent))