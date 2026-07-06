#Write a program which display first 10 even numbers on screen

def PrintEvenNumber():
    count = 1
    
    for i in range(1,100):      # range will run from 1 to 100 and check for even numbers
        if (count <=10):        #  condition to run it till count is 10 so that it will print only 10 even numbers
            if(i%2 ==0):
                print(i)
                count +=1

      

def main():
    PrintEvenNumber()
   

if __name__ == "__main__":
    main()            