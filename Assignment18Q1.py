#Program which accept N number from user and store it into list and return addition of all elements from that list

def AdditionOfNumbers(Numbers):
    sum=0
    for i in Numbers:
        sum= sum+i
    return sum    


def main():
    arr= list()
    number= int(input("Enter number of element to store in list"))

    for i in range(0,number):
        z= int(input("Enter element in list"))
        arr.append(z)
   
    print(arr) 

    ret= AdditionOfNumbers(arr)
    print("sum is",ret)


if __name__ =="__main__":
    main()


