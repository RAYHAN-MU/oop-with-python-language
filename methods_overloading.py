class Student:
    def __init__(self, name, id, department, section): 
        self.name = name
        self.id = id
        self.department = department
        self.section = section 

    def metover(self,*numbers):
        for num in numbers:
            if isinstance(num,(int,float)):
               print(f"Your number is {num}") 
            else:
                 print(f"Your string is {num}")
obj=Student("Rayhan Ahmed", 25, "CSE", "A")
obj.metover(2, 3, 4, 5, 6, 7) 
obj.metover(3,"rayhan ahmed")
