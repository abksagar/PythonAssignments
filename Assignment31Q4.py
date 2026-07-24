#Program to create a new log file after every ten minute. File name should contain current date and time and 
# File should contain Log file Created sucessfully message with Creation time 

import schedule
import time
import datetime

def NewLogFile():

    currentTime= datetime.datetime.now()
    timestamp = currentTime.strftime('%Y-%m-%d %I:%M:%S %p')
    LogFileName ="MarvellousLog_%s"%(currentTime)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj= open(LogFileName,"w")
    fobj.write("Log File Created Sucessfully.\n")
    fobj.write("Creation Time"+timestamp+"\n")

    fobj.close()

def main():
    schedule.every(1).minute.do(NewLogFile)  

    while True:
        schedule.run_pending()
        time.sleep(1)  

if __name__ == "__main__":
    main()        



