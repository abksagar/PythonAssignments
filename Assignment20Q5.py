import threading
def Display(No):

    for i in range(1,No+1):
        print(i)

def DisplayReverse(No):

    for i in range(No,0,-1):
        print(i) 

def main():

    t1= threading.Thread(target=Display,args=(50,),name="Thread1") 
    t2= threading.Thread(target=DisplayReverse,args=(50,),name="Thread2")   

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ =="__main__":
    main()               