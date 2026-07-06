#Program which accept 1 number and return addition of its factors 


def AdditionOfFactors(Num):
    sum=0
   
    for i in range(1,Num):
        if(Num % i == 0):
            sum=sum+i
            
    return sum

def main():
    number= int(input("Enter number"))
    ret= AdditionOfFactors(number)
    print("---",ret)            

if __name__ =="__main__":
    main()
