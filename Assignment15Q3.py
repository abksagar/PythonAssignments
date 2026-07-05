#lambda using filter which aceept list and return list of odd number 



IsOdd= lambda numbers : list(filter(lambda num : num%2 !=0 ,numbers))


def main():

    numbers= list(map(int,input("Enter number ").split()))
    result= IsOdd(numbers)
    print("Odd numbers are:",result)

if __name__ == "__main__":
    main()    


    