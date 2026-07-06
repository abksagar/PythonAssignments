

def NumberPatter(Num):

    for i in range(1,Num+1):
        for j in range(1,i+1):
          print(j,end=" ")
        print(" ")  




def main():
    number= int(input("Enter number:"))
    NumberPatter(number)

if __name__ =="__main__"  :
    main()       