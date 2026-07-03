#accept radius of circle and calculate area of circle

def AreaOfCircle(radius):
    area=3.14*radius*radius
    return area

def main():
    radius = int(input("Enter radius of circle: "))
    result= AreaOfCircle(radius)
    print(result)

if __name__ == "__main__":
    main()