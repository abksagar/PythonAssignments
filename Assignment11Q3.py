#Write a program which accept one number and print sum of digits

def SumOfDigits(num):
    sum=0
    while(num>0):
        sum=sum+num%10
        num=num//10
    return sum

def main():
    number = int(input("Enter a number: "))
    result = SumOfDigits(number)
    print(result)

if __name__ == "__main__":
    main()