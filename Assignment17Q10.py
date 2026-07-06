
def AdditionOfDigit(Num):
    sum=0
    while(Num >0):
        sum=sum+ Num%10
        Num= Num//10
    return sum

def main():
    number= int(input("Enter Number"))
    ret= AdditionOfDigit(number)
    print("Addition of digits are:",ret) 

if __name__ =="__main__":
    main()