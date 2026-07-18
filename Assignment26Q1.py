class Demo:
    Value=0

    def __init__(self,no1,no2):
        self.no1= no1
        self.no2=no2

    def fun(self):
        print(self.no1,"and",self.no2)

    def gun(self):
        print(self.no1,"and",self.no2) 

obj1 = Demo(11,12)
obj2= Demo(51,52)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()

