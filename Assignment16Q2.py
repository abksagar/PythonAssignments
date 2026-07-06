#Write a program which has one function named as ChkNum() which accept one parameter as Number and display even or odd

def ChkNum(No):

    if No%2==0:
        print("Even number")
    else:
        print("Odd number")

def main():
    No= int(input("Enter number:"))
    ChkNum(No)

if __name__ == "__main__":
    main()            