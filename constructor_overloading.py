class student:
    def __init__(self,*info):
        if len(info)==3:
            self.name=info[0]
            self.id=info[1]
            self.department=info[2] 
            print(f"your name is {self.name}\n your id is  {self.id}\n your department is {self.department}")
        elif len(info)==2:
            self.name=info[0]
            self.id=info[1]
            print(f"your name is {self.name} your department is  {self.id}")
        else:
           print("your name is  {self.name}")
objcl=student("rayhan ahmed",25)
  
        