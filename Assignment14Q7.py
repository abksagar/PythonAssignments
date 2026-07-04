#lambda function which accept one numbner and return True if divisble by 5 

IsDivisble= lambda num : True if num %5==0 else False

def main():
    number = int(input("Enter a number: "))
    result = IsDivisble(number)
    print(result)

if __name__ == "__main__":
    main()        

