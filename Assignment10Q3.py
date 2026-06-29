#Program to accept 1 number and print factorial of that number

def Factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def main():
    number = int(input("Enter a number: "))
    result= Factorial(number)
    print(result)

if __name__ == "__main__":
    main()