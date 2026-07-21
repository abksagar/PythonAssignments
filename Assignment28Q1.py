#Write a program which accept file name from user and count how many lines are present in a file 

import os
import sys

def ReadLineFromFiles(fileName):

    if (os.path.exists(fileName)):
        fobj = open (fileName,"r")
        line_count=0
        for line in fobj:
            line_count+=1

        print(f"Total lines in '{fileName}': {line_count}") 

        fobj.close()

    else:
        print("File is not exist.")    


def main():

    ReadLineFromFiles(sys.argv[1])

if __name__ == "__main__":
    main()







        


