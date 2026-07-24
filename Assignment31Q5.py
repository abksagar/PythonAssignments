#Write a program that accept directory name from user and count number of files inside it 
#write a results in DirectoryCountLog.txt and entry should contain Directory path,Number of Files and Date and time

import os
import datetime
import schedule
import sys
import time

def ScanDirectory(DirectoryName):

    print("Directory Name",DirectoryName)
    Filecount=0
    abs_path = os.path.abspath(os.path.expanduser(DirectoryName))
    FileNameD= "DirectoryCountLog"
    currentTime= datetime.datetime.now()
    timestamp = currentTime.strftime('%Y-%m-%d %I:%M:%S %p')
    if(os.path.exists(abs_path)):
       for Foldername,SubFolderName,FileName in os.walk(abs_path):

          for files in FileName:
            Filecount= Filecount+1

       fobj= open(FileNameD,"a")
       fobj.write("Directory path"+abs_path+"\n")
       fobj.write(f"Number of Files {Filecount}"+"\n")
       fobj.write("Date and time"+timestamp+"\n")

       fobj.close()


    else:
       print("Directory is not exist") 


def main():
     
     if(len(sys.argv)!=2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation is used to count of subdirectory and file")
            print("For better usage please check --u flag")

        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Please execute script as")
            print(" python Filename.py DirectoryName")
            print("Display File Count and Subdirectory count")

     else:  
        schedule.every(1).minute.do(ScanDirectory,sys.argv[1])

        while True:
         schedule.run_pending()
         time.sleep(1) 

if __name__ == "__main__":
    main()          

    




        

        


    





