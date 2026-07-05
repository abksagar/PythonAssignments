#lambda function using reduce which accept list of number and return sum of all numbers from it

from functools import reduce

Sum= lambda numbers: reduce(lambda x,y: x+y, numbers)

def main():
    numbers= list(map(int,input("Enter number").split()))
    result= Sum(numbers)
    print("Sum of numbers is:",result)

if __name__ == "__main__":
    main()