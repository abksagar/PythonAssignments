# lambda function using reduce which accept list of number and return minimum number from it

from functools import reduce

MinimumNumber= lambda numbers: reduce(lambda x,y: x if x<y else y , numbers)

def main():
    numbers= list(map(int,input("Enternumber").split()))
    result= MinimumNumber(numbers)
    print("Minimum number is:",result)

if __name__ == "__main__":
    main()