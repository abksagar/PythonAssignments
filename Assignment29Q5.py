#Write a program which accept file name and word from user and return the count of  occurances of that string in the file 
import os
import sys

def CountOfSearchWord(SourcefileName,SearchWord):

    if (os.path.exists(SourcefileName)):
        fobj = open (SourcefileName,"r")
        count=0


        for line in fobj:
             word=line.split()
             
             if SearchWord in word:
               count += word.count(SearchWord)

        print("Count is ",count)  

        fobj.close()




    else:
        print("Source File is not exist.")    


def main():

    if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to check count of  word is file")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print(" python Filename.py sourcefile.extension  word to search")
            print("source file conent will display count the word")
       

    elif(len(sys.argv)==3):
            CountOfSearchWord(sys.argv[1],sys.argv[2])
    else:
         print("Invalid number of paramter it requires 3 argument ")
         print("Please use --h or --u for more information")        

if __name__ == "__main__":
    main()







        


