#program which accept 1 number and print binary equivalent

def DecimalToBinary(num):
    binary = ""
    if num == 0:
        return "0"
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

def main():
    number = int(input("Enter a number: "))
    result = DecimalToBinary(number)
    print( result)

if __name__ == "__main__":
    main()    
