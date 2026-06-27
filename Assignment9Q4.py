#Write a program to find the cube of a number.

def CubeofNumber(num):
    return num*num*num

def main():
    number= int(input("Enter a number:"))
    result= CubeofNumber(number)
    print(result)

if __name__=="__main__":
    main()