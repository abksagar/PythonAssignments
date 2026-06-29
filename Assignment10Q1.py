#Write a program which accpet one number and print multiplication table of that number.

def Multiplication(num):
    arr = list()
    for i in range(1,11):
        arr.append(num*i)
    return arr
        
def main():
    number= int(input("Enter a number"))
    ret=Multiplication(number)
    print(ret)


if __name__ == "__main__":
    main()    
