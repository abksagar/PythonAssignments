import threading

def EvenListNumber(Number):
    sum=0
    for i in Number:
        if(i%2 == 0):
            sum= sum+i
    print("Even Sum ",sum)        


def OddListNumber(Number):
    sum=0
    for i in Number:
        if(i%2 != 0):
            sum= sum+i
    print("Odd Sum ",sum)



def main():
    numbers=list(map(int,input("Enter number").split()))

    t1= threading.Thread(target=EvenListNumber,args=(numbers,),name="EvenList")
    t2= threading.Thread(target=OddListNumber,args=(numbers,),name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ =="__main__":
    main()    

