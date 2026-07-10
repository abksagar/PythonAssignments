#Write program which accept list of integer and uses Pool.map() to calculate sum of squares from 1 to N for every element in list
import multiprocessing

def CalculateSum(Numbers):
    sum= 0
    for i in range(1,Numbers+1):
        sum = sum + (i**2)

    return sum


def main():
    Result=list()
    numbers= list(map(int,input("Enter input numbers").split()))
    ret= multiprocessing.Pool()
    Result=ret.map(CalculateSum,numbers)

    ret.close()
    ret.join()

    print(Result)


if __name__ =="__main__" :
    main()   
