class Numbers:

    def __init__(self):
        Value= int(input("Enternumber"))
        self.Value= Value
        
    def checkPrime(self):

        if self.Value <= 1:
            return False
        
        for i in range(2,int(self.Value/2)+1):

                if(self.Value % i == 0):
                    return False
   
        return True 

    def Factors(self):

        factor= list()

        for i in range(1,self.Value):
            if(self.Value % i ==0):
                factor.append(i)

        return factor

    def SumFactor(self):
        sum= 0

        for i in range(1,self.Value):
            if(self.Value % i ==0):
                sum= sum+i
        return sum

    def chkPerfect(self):

        if self.Value == self.SumFactor():
            return True
        else:
            return False
        
Obj1= Numbers()
prime= Obj1.checkPrime()
print("number is Prime",prime)
print("Factors are",Obj1.Factors())
print("Sum is",Obj1.SumFactor())
print("Number is perfect",Obj1.chkPerfect())


