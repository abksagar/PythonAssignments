#Write a program which accept number from user and return true if number is divisible by 5 else false 

def CheckNumberDivisibleBy5(No1):
    if No1 % 5 ==0:
        return True
    else:
        return False
      

def main():
   number = int(input("Enter a number:"))
   result= CheckNumberDivisibleBy5(number)
   print(result)

if __name__ == "__main__":
    main()            