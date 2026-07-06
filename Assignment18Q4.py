#Program which accept N number from user and store it into list. Accept another number from user and return frequency 
def Frequency(Numbers,search):
    count=0
    for i in Numbers:
        if(search == i):
            count = count+1
    return count    
    


def main():
    arr= list()
    number = int(input("Enter total numbers to be store in list"))

    for i in range(0,number):
        num= int(input("Enter number to add"))
        arr.append(num)


    search= int(input("Enter number to Search"))

    ret= Frequency(arr,search)  
    print("Frequency is",ret)  


if __name__ =="__main__":
    main()