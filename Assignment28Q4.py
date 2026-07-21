#Write a program which accept 2 file name 1st file as source and 2nd as new file and copy content from first in 2nd file

import os
import sys

def CopyContentOfFile(SourcefileName,CopyFile):

    if (os.path.exists(SourcefileName)):
        fobj = open (SourcefileName,"r")

        fobj2 = open(CopyFile,"w")

        for line in fobj:
            fobj2.write(line)


        fobj.close()
        fobj2.close()
        print(f"Content successfully copied from '{SourcefileName}' to '{CopyFile}'.")

    else:
        print("Source File is not exist.")    


def main():

    if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to copy source file conent into destination file")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print("python python Filename.py sourcefile.extension  destinationfile.extention")
            print("source file conent will get copied in destination file")
       

    elif(len(sys.argv)==3):
            CopyContentOfFile(sys.argv[1],sys.argv[2])
    else:
         print("Invalid number of paramter it requires 3 argument ")
         print("Please use --h or --u for more information")        

if __name__ == "__main__":
    main()







        


