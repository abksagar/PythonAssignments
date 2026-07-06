
def PrintPatter(Num):

    for i in range(1,Num+1):
        for j in range(1,Num+1):
            print(j,end=" ")
        print(" ")        


def main():
    number= int(input("Enter number:"))
    PrintPatter(number)

if __name__ =="__main__":
    main()    