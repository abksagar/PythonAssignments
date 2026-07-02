#Accept two number and print addition substraction multiplication and division of those two numbers

Addition = lambda a,b : a+b
Substraction = lambda a,b : a-b 
Multiplication = lambda a,b : a*b
Division = lambda a,b : a/b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Addition of two numbers is: ",Addition(num1,num2))
    print("Substraction of two numbers is: ",Substraction(num1,num2))
    print("Multiplication of two numbers is: ",Multiplication(num1,num2))
    print("Division of two numbers is: ",Division(num1,num2))

if __name__ == "__main__":
    main()