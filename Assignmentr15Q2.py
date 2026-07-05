#lambda function using filter which accept list of number   and return list of even number from it

#Even = lambda numbers: list(filter(lambda num: num % 2 == 0, numbers))

def main():
    numbers1 = list(map(int, input("Enter numbers separated by space: ").split()))
    #result = Even(numbers)
    result = list(filter(lambda num: num % 2 == 0, numbers1))
    #result = even(numbers)
    print("Even numbers are:", result)
    
if __name__ == "__main__":
    main()