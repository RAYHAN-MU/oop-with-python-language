class student:
    def __init__(self,**info):
        if len(info)==3:
            self.name=info["name"]
            self.id=info["id"]
            self.department=info["dept"] 
            print(f"your name is {self.name}\n your id is  {self.id}\n your department is {self.department}")
        elif len(info)==2:
            self.name=info["name"]
            self.dept=info["dept"]
            print(f"your name is {self.name} your department is  {self.dept}")
        else:
           print("your name is  {self.name}")
objcl=student(name="rayhan ahmed",dept="cse")
  
        