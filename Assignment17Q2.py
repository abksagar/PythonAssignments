#write a program which accept number and display * of that number on screen in rows and columns

def PrintStar(No1):

    for i in range(0,No1):
        for j in range(0,No1):
            print("*",end=" ")
        print("")   

def main():
    number = int(input("Enter Number"))
    PrintStar(number)    

if __name__ == "__main__":
    main()            