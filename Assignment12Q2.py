#Accept a number and print its factors

def Factors(num):
    arr=list()
    for i in range(1,num+1):
        if(num%i==0):
            arr.append(i)
    return arr

def main():
    number = int(input("Enter a number: "))
    result = Factors(number)
    print(*result)

if __name__ == "__main__":
    main()           