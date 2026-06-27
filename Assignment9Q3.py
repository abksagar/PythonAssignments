#Program which accept 1 numnber and print square of that number

def SquareofNumber(num):
    return num*num

def main():
    number = int(input("Enter a number: "))
    result = SquareofNumber(number)
    print(result)

if __name__=="__main__":
    main()