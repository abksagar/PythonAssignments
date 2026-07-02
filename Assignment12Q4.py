#Accpet one number and prints that many numbers starting from 1

def PrintNumbers(num):
    arr = list()
    for i in range(1,num+1):
        arr.append(i)   

    return arr

def main():
    number = int(input("Enter a number: "))
    result = PrintNumbers(number)
    print(*result)

if __name__ == "__main__":
    main()        