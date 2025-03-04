class properti:

    def __init__(self,name,color):
        self.name=name
        self.color=color
    def add(self,number,clr):
        number=number/2
        colors=clr
        colors[0]='gray'
        print(f"your number {number}") 
        print(f"your update color {colors}")
num=10
color=['red','green','yellow','black'] 
print(f"your number {num} \n and your color {color}")

obj=properti(num,color)
obj.add(num,color)

