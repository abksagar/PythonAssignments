#Write a program that schedule schedule a task for every minute which write current date and time into a file named marvellous.txt new entries append without removing previous entries
import schedule
import time
import datetime

def Display():
    formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    
    logFileName= "Marvellous.txt"

    fobj= open(logFileName,"a")
    fobj.write("Task Executed at: "+formatted_time +"\n")


    fobj.close()

def main():

     schedule.every(5).minute.do(Display)

     while True:
        schedule.run_pending()
        
        time.sleep(1)

if __name__ =="__main__":
    main()        


