#Program which accept N number from user and store it into list Return max number from list 

def MaxNumber(Number):
    Max=Number[0]
    for i in Number:
        if(i > Max):
            Max=i
    return Max



def main():
    arr= list()
    number= int(input("Enter Number of element to store in list"))

    for i in range(0,number):
        numbers= int(input("List Element"))
        arr.append(numbers)
    #print("--->",arr)

    ret= MaxNumber(arr)
    print("MAX",ret)


if __name__ =="__main__":
    main()


