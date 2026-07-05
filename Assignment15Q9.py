# lambda function using reduce  which accept list of numbers  and return produce of all numbers

from functools import reduce

Product = lambda numbers: reduce(lambda x,y: x*y ,numbers)

def main():
    numbers= list(map(int,input("Enter numbers ").split()))
    result= Product(numbers)
    print("Product of all numbers is:",result)


if __name__ == "__main__":
    main()    