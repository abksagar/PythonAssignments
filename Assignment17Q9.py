
def NumberofDigit(Num):
    count=0
    while(Num>0):
        count= count+1
        Num= Num//10
    return count  

def main():
    number= int(input("Enter Number"))
    ret= NumberofDigit(number)
    print("count is",ret)

if __name__ =="__main__":
    main()