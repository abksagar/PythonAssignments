import threading


def EvenFactor(Num):
    factor= list()
    evenFactor= list()
    sum= 0
        
    for i in range(1,Num+1):
            if(Num%i == 0):
                factor.append(i) 
        
    for i in factor:
        if(i%2==0):
            #evenFactor.append(i)
            sum= sum+i

    print("Sum of Even factor",sum)



def OddFactor(Num):
    factor= list()
    OddFactor= list()
    sum=0
        
    for i in range(1,Num+1):
            if(Num%i == 0):
                factor.append(i) 
        
    for i in factor:
        if(i%2 !=0):
            #OddFactor.append(i)
            sum=sum+i

    print("Sum of odd factor",sum)



def main():
    Number= int(input("Enter Nunmber"))

    # EvenFactor(Number)
    # OddFactor(Number)
    t1= threading.Thread(target=EvenFactor,args=(Number,),name="EvenFactor")
    t2= threading.Thread(target=OddFactor,args=(Number,),name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")
    
 
if __name__ =="__main__":
    main()    


               


         