from audioop import mul
import addition as add
import subtraction as subtract
import multiplication as multiply
import division as divide
import exceptions

CalculatorInputError = exceptions.CalculatorInputError
FunctionSelectionError = exceptions.FunctionSelectionError

def ComputeMathFunction(selection):
    if selection == 1:
        print("{} + {} = {}".format(num1,num2,add.add(num1,num2)))
    elif selection == 2:
        print("{} - {} = {}".format(num1,num2,subtract.subtract(num1,num2)))
    elif selection == 3:
        print("{} X {} = {}".format(num1,num2,multiply.multiply(num1,num2)))
    else:
        print("{} / {} = {}".format(num1,num2,divide.divide(num1,num2)))

def FunctionToPerform(selection):
    if (selection <= 0) or (selection >= 5):
        input("Must be a number between 1 and 4: ")
    elif (selection == 1):
        print("You've chosen to add")
    elif (selection == 2):
        print("You've chosen to subtract")
    elif (selection == 3):
        print("You've chosen to multiply")
    elif (selection == 4):
        print("You've chosen to divide")


user_function = input("Please choose a math function to perform: 1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide")
try:
    user_selection = int(user_function)
except ValueError:
    print("Selection must be a number")

try:
    FunctionToPerform(user_selection)
except FunctionSelectionError:
    print("error")
    

num1 = input("Choose the first number: ")
try:
    num1 = int(num1)
except CalculatorInputError:
    print("Error, please enter a number")


num2 = input("Choose the second number: ")
try:
    num2 = int(num2)
except CalculatorInputError:
    print("error")
finally:
    print("You chose {}".format(num2))
        

print(ComputeMathFunction(user_selection))