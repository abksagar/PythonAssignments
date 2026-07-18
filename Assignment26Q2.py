class Circle:

    PI= 3.14
    def __init__(self,Radius=0,Area=0,Circumference=0):
        self.Radius= Radius
        self.Area= Area
        self.Circumference= Area

    def Accept(self):
        self.Radius= int(input("Enter radius of circle"))    
        return self.Radius 
    
    def CalculateArea(self):
        self.Radius = self.Accept()
        self.Area= self.PI *self.Radius *self.Radius
        #print("Area is",Area)

    def CalculateCircumference(self):
        self.Circumference= 2*self.PI*self.Radius
        #print(f"Circumference: {self.Circumference:.2f}")
    
    def Display(self):
        print("Radius of circle ",self.Radius)
        print("Area of circle",self.Area)
        print(f"Circumference of circle:{self.Circumference:.2f}")


        
CObje= Circle()
CObje.CalculateArea()
CObje.CalculateCircumference()
CObje.Display()

CObje1= Circle()
CObje1.CalculateArea()
CObje1.CalculateCircumference()
CObje1.Display()
