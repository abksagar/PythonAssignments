#Program that accept message from user and schedule it after 5 seconds

import schedule
import sys
import time

def DisplayMessage(Message):

     print(Message)
   

     
def main():
   
   schedule.every(5).seconds.do(DisplayMessage,sys.argv[1])
   while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__"  :
   main()      




