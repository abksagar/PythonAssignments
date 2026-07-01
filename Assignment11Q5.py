#accept 1 number and check palindrome or not

def CheckPalindrome(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num=num//10
    return rev

def main():
    number = int(input("Enter a number: "))
    result = CheckPalindrome(number)
    if (number == result):
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

if __name__ == "__main__":
    main()

