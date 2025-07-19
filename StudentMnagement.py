class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}
    
    def enroll_course(self, course_name, grade=None):
        self.courses[course_name] = grade
        print(f"{self.name} enrolled in {course_name}")
    
    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade updated for {course_name}")
        else:
            print(f"Not enrolled in {course_name}")
    
    def calculate_gpa(self):
        total = 0
        count = 0
        for grade in self.courses.values():
            if grade is not None:
                total += grade
                count += 1
        return total / count if count > 0 else 0
    
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses Enrolled:")
        for course, grade in self.courses.items():
            print(f"  - {course}: {grade if grade is not None else 'No grade yet'}")
        print(f"Current GPA: {self.calculate_gpa():.2f}")

# ব্যবহার
student1 = Student("Alice", "S001")
student1.enroll_course("Math")
student1.enroll_course("Physics", 85)
student1.update_grade("Math", 90)
student1.display_info()
