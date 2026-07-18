class Arithmetic:

    def __init__(self,value1=0,value2=0):
        self.value1=value1
        self.value2=value2

    def Accept(self):
        self.value1= int(input("Enter first number")) 
        self.value2 = int(input("Enter second number")) 

    def Addition(self):
        add = self.value1+ self.value2
        return add
    
    def Substraction(self):
        sub= self.value1- self.value2
        return sub
    
    def Multiplication(self):
        mult= self.value1 * self.value2
        return mult
    
    def Division(self):

        if(self.value2 == 0):
            return "Division by zero not possible"
        return self.value1/self.value2
    
obj1 = Arithmetic()
obj1.Accept()    

print(f"{obj1.Addition()}")
print(f"{obj1.Substraction()}")
print(f"{obj1.Multiplication()}")
print(f"{obj1.Division()}")

obj2 = Arithmetic()
obj2.Accept()    

print(f"{obj2.Addition()}")
print(f"{obj2.Substraction()}")
print(f"{obj2.Multiplication()}")
print(f"{obj2.Division()}")


