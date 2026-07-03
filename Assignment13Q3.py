#accept number check whether its perfect number or not

def CheckPerfectNumber(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        print("perfect number")
    else:
        print("not a perfect number")

def main():
    number=int(input("Enter a number: "))
    CheckPerfectNumber(number)

if __name__=="__main__":
    main()        