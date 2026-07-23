#Write a program that print current date and time after every 1 minute
import schedule
import time
import datetime

def Display():
    formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    print("Current Date And Time:", formatted_time)

def main():

     schedule.every(1).minute.do(Display)

     while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()        


