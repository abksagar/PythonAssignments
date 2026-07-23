#Write a program which accept file name from user and check whether file exist in current directory or not
import os
import sys

def FileExistInDirectory(FileName):

    filePath = os.path.join(os.getcwd(), FileName)

    if(os.path.isfile(filePath)):
        print(f"{FileName} exist ")
    else:
        print("File name is not exist")

def main():

     if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to check whether File is present or not")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print(" python Filename.py Filename")
            print("This will check whether file is present or not")
        else:  
            FileExistInDirectory(sys.argv[1])  
     else:
        print("Invalid number of arguments.")
        print("Use --h or --u for details.")

    

if __name__ == "__main__":
    main()    

