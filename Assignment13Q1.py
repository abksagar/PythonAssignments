#Program which accept length and widht of rectangle and calculate area of rectangle

def AreaOfRectangle(length,width):
    area=length*width
    return area

def main():
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))
    result= AreaOfRectangle(length,width)
    print(result)

if __name__ == "__main__":
    main()        