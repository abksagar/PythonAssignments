#Write a program which accept file name and display content of file line by line on screen  

import os
import sys

def ReadLineFromFiles(fileName):

    if (os.path.exists(fileName)):
        fobj = open (fileName,"r")

        #FileContent= fobj.read()

        for line in fobj:
            print(line,end="")

       

        fobj.close()

    else:
        print("File is not exist.")    


def main():

    ReadLineFromFiles(sys.argv[1])

if __name__ == "__main__":
    main()







        


