import multiprocessing
import os

def SumOfEvenNumbers(Numbers):
    print("Process id",os.getpid())
    sum=0

    for i in range(2,Numbers+1,2):
        sum= sum+i

    return sum


def main():
    numbers= list(map(int,input("Enter Number of list").split()))

    pobj= multiprocessing.Pool()
    ret= pobj.map(SumOfEvenNumbers,numbers)

    pobj.close()
    pobj.join()

    print("Result",ret)

if __name__ =="__main__":
    main()

