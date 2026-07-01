#Accept number and print reverse 

def ReverseNumber(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num=num//10
    return rev

def main():
    number = int(input("Enter a number: "))
    result = ReverseNumber(number)
    print(result)

if __name__ == "__main__":
    main()    