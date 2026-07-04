#lambda which accept three number and return largest number

LargestNumber = lambda x,y,z : x if x>y and x>z else y if y>z and y>x else z

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    number3 = int(input("Enter third number: "))
    result = LargestNumber(number1, number2, number3)
    print("Largest number is", result)


if __name__ == "__main__":
    main()    