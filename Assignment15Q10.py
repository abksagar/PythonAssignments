#lambda function using filter which accept list of number and return count of even number from it

CountOfEven = lambda numbers: list(filter(lambda num: num%2 ==0 ,numbers))

def main():
    numbers= list(map(int,input("Enter number ").split()))
    result= CountOfEven(numbers)
    print("Count of even numbers are:",len(result))

if __name__ == "__main__":
    main()    