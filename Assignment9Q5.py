# Program which accept 1 number and check whether its divisble by 3 and 5 

def CheckDivisible(num):

    if(num % 3 == 0 and num % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    number=int(input("Enter a number: "))
    CheckDivisible(number)

if __name__=="__main__":
    main()