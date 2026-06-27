#Write a function which contains a function ChkGreater() which accept two number and print greater number from two number.

def chkGreater(num1, num2):
    if num1 > num2:
        print(num1 ,"is greater")
    elif num2 > num1:
        print(num2 ,"is greater")
    else:
        print("Both numbers are equal.")

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    chkGreater(number1, number2)  

if __name__=="__main__" :
    main()     