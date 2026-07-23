#Write a program that schedule following task Print lunch every day 1 pm and print Wrap up every day 6 PM
import schedule
import time

def Display():
    print("Lunch Time...")

def Wrap():
    print("Wrap Up ")    

def main():

     schedule.every().day.at("13:00").do(Display)
     schedule.every().day.at("18:00").do(Wrap)


     while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()        


