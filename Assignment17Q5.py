#Check whether number is prime or not

def checkPrime(Num):

    if(Num > 1) :
        for i in range(2,Num):
            if(Num % i) == 0 :
                print("not prime")
                break
        else:
            print("Prime")

    else :
        print("Not prime")            

def main():
    number= int(input("Enter number"))
    checkPrime(number)

if __name__ == "__main__":
    main()    

    