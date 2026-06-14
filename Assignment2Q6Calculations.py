
print("Enter the first number: ")
number1 = int(input())
print("Enter the second number: ")
number2 = int(input())

#Addition of two numbers
addition = number1 + number2
print("The addition of two numbers is: ", addition)

#Subtraction of two numbers
subtraction = number1 - number2
print("The subtraction of two numbers is: ", subtraction)

#Multiplication of two numbers
multiplication = number1 * number2
print("The multiplication of two numbers is: ", multiplication)

#Division of two numbers
if number2 != 0:
    division = number1 / number2
    print("The division of two numbers is: ", division)
else:
    print("Division by zero is not allowed.")
