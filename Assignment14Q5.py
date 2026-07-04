#lambda function which accept one number return True if number is even otherwise return False

IsEven = lambda num : True if num%2==0 else False

def main():
    number = int(input("Enter a number: "))
    result = IsEven(number)
    print(result)

if __name__ == "__main__":
    main()