# lambda function using filter  which accept list of numbers  and return list of numbe divisble by both 3 & 5

DivisibleBy3And5= lambda numbers: list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

def main():
    numbers= list(map(int,input("Enter numbers ").split()))
    result= DivisibleBy3And5(numbers)
    print("Numbers divisible by both 3 and 5 are:",result)


if __name__ == "__main__":
    main()    