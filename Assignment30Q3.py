#Write a program that schedule a function to print Coding Kar..!
import schedule
import time

def Display():
    print("Coding Kar..!")

def main():

     schedule.every(30).minute.do(Display)

     while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()        


