class car:
    def __init__(self,color,model):
        self.color=color
        self.model=model 
    def display(self):
        print(f"your car color is {self.color}\n your car model is  {self.model}")
    def comapre(self,upmodel):
        if self.model==upmodel.model:
            print(f"your car model is equal")
        else:
            print(f"your car model is not equal") 


carobj1=car("white","bmw")
carobj2=car("red","bmws")
carobj1.comapre(carobj2)