# There are three types of constructor:
# 1.Default Constructor
# 2.Parameterized Constructor
# 3.Default value constructor

# Default constructor e constructor er modhe self chara onno kono value thakena.ar object create kore object diye directly call kora jay.


class Student:
    def __init__(self):  
        print("Default constructor is called")
    
    def display(self):
        print("This is default constructor example")

s1 = Student()  
s1.display()  

  

# Paramiterized constructor parametter ney and object er atribute initialize kore
class Employee:
    def __init__(self, name, id):
        self.name = name  # instance variable
        self.id = id     # instance variable
        print(f"Employee {self.name} with ID {self.id} created")


emp1 = Employee("Rahim", 101)  # Output: Employee Rahim with ID 101 created
emp2 = Employee("Karim", 102)  # Output: Employee Karim with ID 102 created








#Default Value constructor
class Student:

    def __init__(self, name="Unknown", id=0, department="CSE"):
        self.name = name
        self.id = id
        self.department = department
        print(f"Student created: {self.name}, ID: {self.id}, Dept: {self.department}")


s1 = Student()
# Output: Student created: Unknown, ID: 0, Dept: CSE


s2 = Student("Rahim")
# Output: Student created: Rahim, ID: 0, Dept: CSE


s3 = Student("Karim", 101)
# Output: Student created: Karim, ID: 101, Dept: CSE


s4 = Student("Fatima", 102, "EEE")
# Output: Student created: Fatima, ID: 102, Dept: EEE
