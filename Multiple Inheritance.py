class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}, age {self.age}")

class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
    
    def work(self):
        print(f"Employee ID {self.employee_id} salary {self.salary}")

class Manager(Person, Employee):  # Inherits from both classes
    def __init__(self, name, age, employee_id, salary, department):
        Person.__init__(self, name, age)          # Call Person's __init__
        Employee.__init__(self, employee_id, salary) # Call Employee's __init__
        self.department = department
    
    def manage(self):
        print(f"{self.name} is managing {self.department} department")

# Usage
manager = Manager("Rahi", 35, "77", 80000, "IT")
manager.introduce()  # From Person class
manager.work()      # From Employee class
manager.manage()    # From Manager class
