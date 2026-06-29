#which accept 1 number and print all even number upto that number 

def PrintEvenNumbers(num):
    arr= list()
    for i in range(1,num+1):
        if( i%2 == 0):
            arr.append(i)
    return arr

def main():
    number = int(input("Enter a number: "))
    result = PrintEvenNumbers(number)
    print(result)

if __name__ == "__main__":
    main()