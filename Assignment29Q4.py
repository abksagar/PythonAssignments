#Write a program which accept 2 file name and compare content of both file if content is same display sucess otherwise Failure
import os
import sys

def CompareFile(SourcefileName,CopyFile):

    if (os.path.exists(SourcefileName) and os.path.exists(CopyFile)):
        fobj = open (SourcefileName,"r")

        fobj2 = open(CopyFile,"r")

        Data= fobj.read()
        Data2= fobj2.read()

        if(Data == Data2):
             print("SUCCESS")
        else:
             print("FAILURE")     


        fobj.close()
        fobj2.close()


    else:
        print("Source File is not exist.")    


def main():

    if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to check content of source file and destination file")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print("python python Filename.py sourcefile.extension  destinationfile.extention")
            print("check source file conent with destination file")
       

    elif(len(sys.argv)==3):
            CompareFile(sys.argv[1],sys.argv[2])
    else:
         print("Invalid number of paramter it requires 3 argument ")
         print("Please use --h or --u for more information")        

if __name__ == "__main__":
    main()







        


