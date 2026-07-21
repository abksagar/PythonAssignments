#Write a program which accept file name and word from user and check whether word in present in file or not 
import os
import sys

def SearchWord(SourcefileName,SearchWord):

    if (os.path.exists(SourcefileName)):
        fobj = open (SourcefileName,"r")
        Flag= False


        for line in fobj:
             word=line.split()
             
             if SearchWord in word:
               Flag= True
               break  

        fobj.close()

        if Flag:
            print(f"{SearchWord} is present in a file {SourcefileName}")
        else:
            print(f"{SearchWord} is not present in a file {SourcefileName}")



    else:
        print("Source File is not exist.")    


def main():

    if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to check whether word is present or not")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print(" python Filename.py sourcefile.extension  word to search")
            print("source file conent will search the word")
       

    elif(len(sys.argv)==3):
            SearchWord(sys.argv[1],sys.argv[2])
    else:
         print("Invalid number of paramter it requires 3 argument ")
         print("Please use --h or --u for more information")        

if __name__ == "__main__":
    main()







        


