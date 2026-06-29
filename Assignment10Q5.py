#which accept 1 number and print all odd number upto that number 

def PrintOddNumbers(num):
    arr= list()
    for i in range(1,num+1):
        if( i%2 != 0):
            arr.append(i)
    return arr

def main():
    number = int(input("Enter a number: "))
    result = PrintOddNumbers(number)
    print(result)

if __name__ == "__main__":
    main()