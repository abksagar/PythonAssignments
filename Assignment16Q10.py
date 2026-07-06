#Write a program which accept name from user and print length of name on screen

def Printlength(Name):
    #print("Length of name is:",len(Name))   #---> Direct length 
    count=0

    for i in Name:
        count +=1

    return count    
         

def main():
    name= input("enter name:")
    result= Printlength(name)
    print("Length of name is:",result)
   

if __name__ == "__main__":
    main()            