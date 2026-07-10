#Write program that calculates factorials of multiple numbers simulteneously 
import multiprocessing
import os

def Factorials(Numbers):
    print("Process with pid",os.getpid())
    fact= 1
    for i in range(1,Numbers+1):
        fact = fact + (fact*1)

    return fact


def main():
    Result=list()
    numbers= list(map(int,input("Enter input numbers").split()))
    ret= multiprocessing.Pool()
    Result=ret.map(Factorials,numbers)

    ret.close()
    ret.join()

    print(Result)


if __name__ =="__main__" :
    main()   
