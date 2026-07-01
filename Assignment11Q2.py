#Accept one number and print count of digits in that number

def CountDigits(num):
    count=0
    while(num>0):
        count=count+1
        num=num//10
    return count

def main():
    number = int(input("Enter a number: "))
    result = CountDigits(number)
    print(result)

if __name__ == "__main__":
    main()
