# star print

def PrintStarPattern(Num):

    for i in range(Num,0,-1):
            print("*" * i)

def main():
    number= int(input("Enter number:"))
    PrintStarPattern(number)

if __name__ == "__main__":
    main() 