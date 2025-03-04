class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department
    def display(self):
        print(f"Your student name is {self.name}")
        print(f"Your student ID is {self.student_id}")
        print(f"Your student department is {self.department}")
obj1 = Student("Rayhan Ahmed", 25, "CSE")
print(obj1.name) 
obj1.display()
