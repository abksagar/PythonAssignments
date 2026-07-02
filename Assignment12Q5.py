#Accpet one number and prints that many numbers in reverse order

def PrintReverseNumber(num):
    arr =list()
    for i in range(num,0,-1):
        arr.append(i)
    return arr

def main():
    number = int(input("Enter a number: "))
    result = PrintReverseNumber(number)
    print(*result)

if __name__ == "__main__":
    main()