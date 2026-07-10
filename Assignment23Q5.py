#Factorial of numbers

import multiprocessing
import os

def FactorialNumbers(Numbers):

    print("Process id",os.getpid())
    fact=1

    for i in range(1,Numbers+1):
        fact= fact*i

    return fact

def main():
    result= list()
    numbers= list(map(int,input("enter numbers").split()))

    pobj= multiprocessing.Pool()  
    result= pobj.map(FactorialNumbers,numbers)   

    pobj.close()
    pobj.join()

    print(result)

if __name__ == "__main__":
    main()    