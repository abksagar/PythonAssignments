#for every number in list count how many prime numbers exist between 1 and N using multithreading pool 
import multiprocessing
import os

def PrimeNumbers(Numbers):
    print("Process with pid",os.getpid())
    if(Numbers > 1): 

        for i in range(2,int(Numbers/2)+1):
            if(Numbers %i == 0):
                return False
             
        return True
    
def countOfPrime(N):

    primeCount=0

    for i in range(1,N+1):
        if PrimeNumbers(i):
            primeCount+=1

    return primeCount        


def main():
    Result=list()
    numbers= list(map(int,input("Enter input numbers").split()))
    ret= multiprocessing.Pool()
    Result=ret.map(countOfPrime,numbers)

    ret.close()
    ret.join()

    print(Result)


if __name__ =="__main__" :
    main()   
