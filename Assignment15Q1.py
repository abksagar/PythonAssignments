#lambda function USING map() which accept list of numbers and return list of square of numbers

Square = lambda numbers : list(map(lambda x: x*x, numbers))

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    result = Square(numbers)
    print("Square of numbers is", result)

if __name__ == "__main__":
    main()