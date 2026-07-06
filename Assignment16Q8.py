#Write a program which accept number from user and print that number of * on screen

def PrintStar(No1):
    
    for i in range(0,No1):
        print("*")

      

def main():
   number = int(input("Enter a number:"))
   PrintStar(number)
   

if __name__ == "__main__":
    main()            