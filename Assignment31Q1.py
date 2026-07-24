#Program that accept message from user and interval in second schedule a program to display the message repatedly after specific interval 
#Validate interval is greater than 0

import schedule
import sys
import time

def DisplayMessage(Message,Interval):

    Interval = int(Interval)

    if(Interval > 0):

     print(Message)
     print(f"Every {Interval} second")

     
def main():
   
   schedule.every(int(sys.argv[2])).seconds.do(DisplayMessage,sys.argv[1],sys.argv[2])
   while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__"  :
   main()      




