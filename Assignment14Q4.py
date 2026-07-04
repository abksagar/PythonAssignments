
MinimumNumber= lambda num1,num2 : num1 if num1< num2 else num2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = MinimumNumber(number1, number2)
    print("Minimum number is", result)  

if __name__ == "__main__":
    main()      