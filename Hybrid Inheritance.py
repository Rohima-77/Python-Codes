class Person:  # Base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):  # Child class 1
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):  # Child class 2
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
    
    def teach(self):
        print(f"{self.name} is teaching")

class SchoolStaff(Student, Teacher):  # Hybrid inheritance
    def __init__(self, name, age, student_id, teacher_id, role):
        Person.__init__(self, name, age)
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, teacher_id)
        self.role = role
    
    def work(self):
        print(f"{self.name} is working as {self.role}")


staff = SchoolStaff("Rahim", 35, "S123", "T456", "Lab Assistant")
staff.display()  # Person থেকে
staff.study()   # Student থেকে
staff.teach()   # Teacher থেকে
staff.work()    # SchoolStaff থেকে
