#Accept two number and return multiplication 


Multiplication = lambda num1,num2 : num1*num2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = Multiplication(number1, number2)
    print("Multiplication is", result)

if __name__ == "__main__":
    main()