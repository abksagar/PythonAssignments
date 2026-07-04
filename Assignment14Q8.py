#lambda function which accept 2 number and return adddition 

Addition = lambda x,y : x+y

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = Addition(number1, number2)
    print("Addition is", result)

if __name__ == "__main__":
    main()