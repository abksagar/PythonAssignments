
import MarvellousNum as MN


def ListPrime(Numbers):
    sum=0 

    for num in Numbers:
        if MN.ChkPrime(num):
            sum= sum+num
    return sum        

def main():
    arr= list()
    number= int(input("enter number of elements in list"))

    for i in range(0,number):
        num= int(input("Enter number: "))
        arr.append(num)

    ret =ListPrime(arr)
    print("sum of prime number is",ret) 


if __name__ =="__main__":
    main()


