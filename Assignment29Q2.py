#Write a program which accept file name from user and open that file and read entire content on the console
import os
import sys

def DisplayFileContent(FileName):

    if (os.path.exists(FileName)):
        fobj= open(FileName,"r")
        Data= fobj.read()
        print(Data)

        fobj.close()

    else:
        print("File does not exist")    


def main():

     if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to read content of file")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print(" python Filename.py Filename")
            print("This will display entire content of file")
        else:  
            DisplayFileContent(sys.argv[1])  
     else:
        print("Invalid number of arguments.")
        print("Use --h or --u for details.")

    

if __name__ == "__main__":
    main()    

