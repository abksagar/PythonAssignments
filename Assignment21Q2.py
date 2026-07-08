import threading

def MaximumNumber(Numbers):
    Max= Numbers[0]
    
    for i in Numbers:
        if(i > Max):
            Max=i

    print("Max number",Max)     


def MinimumNumber(Numbers):
    Min= Numbers[0]
    
    for i in Numbers:
        if(i < Min):
            Min=i

    print("Min number",Min)        


def main():
    numbers= list(map(int,input("Enter list of elements").split()))

    t1= threading.Thread(target= MaximumNumber,args=(numbers,))
    t2= threading.Thread(target= MinimumNumber,args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()