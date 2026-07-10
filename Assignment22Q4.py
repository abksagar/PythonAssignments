#for every number power of 5
import multiprocessing
import os
import time

def powerOf5(Numbers):
    print("Process with pid",os.getpid())
    sum= 0
    for i in range(1,Numbers+1):
        sum = sum + (i**5)
        
    return sum        
    

def main():
    Result=list()
    numbers= list(map(int,input("Enter input numbers").split()))

    start_time = time.perf_counter()

    ret= multiprocessing.Pool()
    Result=ret.map(powerOf5,numbers)

    ret.close()
    ret.join()

    end_time = time.perf_counter()


    print(Result)
    print(f"time required: {end_time-start_time:.4f}")


if __name__ =="__main__" :
    main()   
