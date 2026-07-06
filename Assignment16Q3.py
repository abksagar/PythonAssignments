#Write a program which has one function named as Add() which accept two parameter as Number and display addition

def Add(No1,No2):

    return No1+No2

def main():
    No1= int(input("Enter first number:"))
    No2= int(input("Enter second number:"))
    result= Add(No1,No2)
    print("Addition is:",result)

if __name__ == "__main__":
    main()            