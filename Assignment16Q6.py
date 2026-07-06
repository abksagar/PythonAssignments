#Write a program which accept number from user and check whether number is +ve -ve or zero 

def CheckNumber(No1):
    if No1 > 0:
        print("Positive number")
    elif No1 < 0:
        print("Negative number")
    else:
        print("Zero")
      

def main():
   number = int(input("Enter a number:"))
   CheckNumber(number)

if __name__ == "__main__":
    main()            