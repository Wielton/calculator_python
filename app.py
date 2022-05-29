import addition as add
import subtraction as subtract
import multiplication as multiply
import division as divide

    
user_function = input("Please choose a math function to perform: 1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide")
try:
    user_function = int(user_function)
except ValueError:
    print("Error, {} is not one of the available selections.  Please try again".format(user_function))
    exit()
finally:
    print("You chose {}".format(user_function))
    
num1 = input("Choose the first number: ")
try:
    num1 = int(num1)
except ValueError:
    print("{} is not a number".format(num1))
finally:
    print("You chose {}".format(num1))

num2 = input("Choose the second number: ")
try:
    num2 = int(num2)
except ValueError:
    print("{} is not a number".format(num2))
finally:
    print("You chose {}".format(num2))
        
    
if user_function == 1:
    
    print("{} + {} = {}".format(num1,num2,add.add(num1,num2)))
elif user_function == 2:
    print("{} + {} = {}".format(num1,num2,subtract.subtract(num1,num2)))
elif user_function == 3:
    print("{} + {} = {}".format(num1,num2,multiply.multiply(num1,num2)))
else:
    print("{} + {} = {}".format(num1,num2,divide.divide(num1,num2)))