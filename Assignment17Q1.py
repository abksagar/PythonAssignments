#Create a module named Arithmetic which contains four functions as Add(), Sub(), Mul(), Div(). All functions accepts two parameters as Number and perform the operation. Write a program which call all the functions from Arithmetic module by accepting the parameters from user. 

import Arithmetic as AM


def main():
    No1= int(input("Enter first number:"))
    No2= int(input("Enter second number:"))
    
    Add = AM.Add(No1,No2)
    print("Addition is:",Add)
    
    Sub = AM.Sub(No1,No2)
    print("Subtraction is:",Sub)
    
    Mult = AM.Mult(No1,No2)
    print("Multiplication is:",Mult)
    
    Div = AM.Div(No1,No2)
    print("Division is:",Div)

if __name__ == "__main__":
    main()
            