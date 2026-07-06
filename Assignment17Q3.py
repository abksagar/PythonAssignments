# write a program which accept number and return factorial of number


def Factorial(No1):
    fact=1
    for i in range(1,(No1+1)):
       fact= fact*i
    
    return fact

def main():
    number= int(input("Enter number"))
    result= Factorial(number)
    print(result)

if __name__ =="__main__":
    main()