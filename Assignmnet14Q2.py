#lambda function which accept one number and return cube 

CubeOfnumber = lambda num : num*num*num

def main():
    number= int (input("Enter number"))
    result= CubeOfnumber(number)
    print("Cube is",result)

if __name__== "__main__":
    main()    