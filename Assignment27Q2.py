class BankAccount:

    ROI= 10.5
    def __init__(self,Name,Amount):
        self.Name= Name
        self.Amount= Amount

    def Display(self):
        print("Account holder name is",self.Name,"And Balance is",self.Amount)   

    def Deposit(self):
        amountAdd= int(input("Enter Amount to deposit")) 
        self.Amount= self.Amount+amountAdd

        return self.Amount

    def Withdraw(self):
        amountWithdraw = int(input("Enter Amount withdraw"))
        if(self.Amount >= amountWithdraw):
            self.Amount= self.Amount - amountWithdraw 
        else:
            print("Balance is not sufficient")  
        return self.Amount     

    def CalculateInterest(self):
        interest =(self.Amount *BankAccount.ROI) /100
        return interest
    
Obj1= BankAccount("An",5000)
Obj1.Deposit()
Obj1.Withdraw()
interestearned= Obj1.CalculateInterest()
print("Interest Earned",interestearned)
Obj1.Display()


Obj2= BankAccount("An",6000)
Obj2.Deposit()
Obj2.Withdraw()
interestearned= Obj2.CalculateInterest()
print("Interest Earned",interestearned)
Obj2.Display()





