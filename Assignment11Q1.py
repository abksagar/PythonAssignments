#Write a program which accept one number and check whether that number is prime or not.

def CheckPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


def main():
    number = int(input("Enter a number: "))
    CheckPrime(number)

if __name__ == "__main__":
    main()    
