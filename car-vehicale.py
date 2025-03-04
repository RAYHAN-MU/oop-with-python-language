class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        self.wheel=4
    def view(self):
        print(self.name)
        print(self.model)
    def update_model(self,model):
        self.model=model
carobj1=car("bmw",2024)
carobj2=car("bmws",2024)

carobj1.view()
carobj2.view()            
carobj2.update_model("asus_model")
carobj2.view()
  
print(carobj1.__dict__) 
print(dir(carobj1))