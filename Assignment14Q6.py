#lambda function which accpet 1 number and return true if its odd

IsOdd = lambda num : True if num % 2 != 0 else False

def main():
    number = int(input("Enter a number: "))
    result = IsOdd(number)
    print(result)

if __name__ == "__main__":
    main()