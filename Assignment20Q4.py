import threading

def Countlowercase(Value):
    count=0
    print("Thread ID",threading.get_ident())
    print("Thread Name",threading.current_thread().name)
    for i in Value:
        if i.islower():
            count=count+1
    print("Lowercase character",count)   

def CountUpperCase(Value):  
    count=0
    print("Thread ID",threading.get_ident())
    print("Thread Name",threading.current_thread().name)
    for i in Value:
        if i.isupper():
            count=count+1
    print("Uppar character",count)

def countDigit(Value):
    count=0
    print("Thread ID",threading.get_ident())
    print("Thread Name",threading.current_thread().name)
    for i in Value:
        if i.isdigit():
            count=count+1
    print("Digit count is",count)


def main():
    inputString = input("Enter string with lower uppar and digits")

    t1= threading.Thread(target=Countlowercase,args=(inputString,),name="Small")  
    t2= threading.Thread(target=CountUpperCase,args=(inputString,),name="Capital")
    t3= threading.Thread(target=countDigit,args=(inputString,),name="Digit") 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ =="__main__":
    main()    


 
