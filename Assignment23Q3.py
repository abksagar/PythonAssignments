#count of even number exists

import multiprocessing
import os

def CountOfEvenNumbers(Numbers):
    print("Process id",os.getpid())
    count=0

    for i in range(2,Numbers+1,2):
        count= count+1

    return count


def main():
    numbers= list(map(int,input("Enter Number of list").split()))

    pobj= multiprocessing.Pool()
    ret= pobj.map(CountOfEvenNumbers,numbers)

    pobj.close()
    pobj.join()

    print("Result",ret)

if __name__ =="__main__":
    main()

