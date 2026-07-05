# lambda function using reduce which accept list of number and return maximum number from it

from functools import reduce

maxNumber= lambda numbers: reduce(lambda x,y: x if x>y else y,numbers)

def main():
    numbers= list(map(int,input("Enter number").split()))
    result= maxNumber(numbers)
    print("Maximum number is:",result)

if __name__ == "__main__":
    main()