#Write a program that scans a specified directory every minute 
#Task should display Directory name Number of files Number of subdirectories Data and time of scanning 

import os
import datetime
import schedule
import sys
import time

def ScanDirectory(DirectoryName):

    print("Directory Name",DirectoryName)
    Filecount=0
    SubdirectoryCount=0
    abs_path = os.path.abspath(os.path.expanduser(DirectoryName))
    if(os.path.exists(abs_path)):
     for Foldername,SubFolderName,FileName in os.walk(abs_path):

        for SubFolder in SubFolderName:
            SubdirectoryCount=SubdirectoryCount+1


        for files in FileName:
            Filecount= Filecount+1

     print("SubDirectories are",SubdirectoryCount)  
     print("Total Files",Filecount) 

     formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

     print("Scan Time"+formatted_time)

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

    




        

        


    





