class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):  # First level inheritance
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} is studying")

class ResearchStudent(Student):  # Second level inheritance
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic
    
    def conduct_research(self):
        print(f"{self.name} is researching on {self.research_topic}")

# Usage
research_student = ResearchStudent("Ali", 25, "77", "Machine Learning")
research_student.display_info()      # From Person
research_student.study()            # From Student
research_student.conduct_research() # From ResearchStudent
