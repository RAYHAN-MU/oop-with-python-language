from multipledispatch import dispatch 

class Calculator:
    pass  # No methods inside class, we define functions outside

@dispatch(int, int) 
def addition(number1, number2):
    print(f"Your output is {number1 + number2}") 

@dispatch(int, int, float)
def addition(number1, number2, number3):
    print(f"Your output is {number1 + number2 + number3}")  # Fixed print

@dispatch(int, str)
def addition(number1, number2):
    print(f"Your output is {number1 + int(number2)}")

# Creating an instance (not needed as methods are outside)
objcal = Calculator()

# Calling functions
addition(2, 3)
addition(4, 5, 3.5)
addition(20, "30")
