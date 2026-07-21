#Write a program which accept file name from user and count words in a file 

import os
import sys

def ReadLineFromFiles(fileName):

    if (os.path.exists(fileName)):
        fobj = open (fileName,"r")
        word_count=0
        for line in fobj:
            word = line.split()
            word_count+= len(word)
           

        print(f"Total words in '{fileName}': {word_count}") 

        fobj.close()

    else:
        print("File is not exist.")    


def main():

    ReadLineFromFiles(sys.argv[1])

if __name__ == "__main__":
    main()







        


