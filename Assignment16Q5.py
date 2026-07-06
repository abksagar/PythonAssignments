#Write a program which display 10 to 1 on screen

def Display():
    result= list()
    for i in range(10,0,-1):
        result.append(i)
    print(*result)    

def main():
   Display()

if __name__ == "__main__":
    main()            