import threading
def Even():
    #print("---",No)
    count=1
    for i in range(2,100,2):
        print(i)
        count=count+1
        if count > 10:
            break

def Odd():
    count=1
    for i in range(1,100,2):
        print(i)
        count= count+1
        if count >10:
            break


def main():

    EvenThread= threading.Thread(target=Even,args=(),name="Even")
    EvenThread.start()

    OddThread= threading.Thread(target=Odd,args=(),name="Odd")
    OddThread.start()

    EvenThread.join()
    OddThread.join()


if __name__=="__main__":
    main()
        
