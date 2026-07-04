#lambda function which accept one number and return square of it 

SquareofNumber = lambda num :num* num


def main():
    number = int(input("Enter a number: "))
    result = SquareofNumber(number)
    print(result)

if __name__ == "__main__":
    main()