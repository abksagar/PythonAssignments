#Program which accpet 1 number and print sum of first N natural numbers

def Sum(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum

def main():
    number = int(input("Enter a number: "))
    result = Sum(number)
    print(result)

if __name__ == "__main__":
    main()