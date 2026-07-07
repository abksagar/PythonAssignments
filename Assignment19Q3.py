
from functools import reduce

FilterData = lambda x : x >=70 and x <=90

IncrementBy10 = lambda x: (x+10)

Product = lambda x,y : x*y


def filterx(Task,Element):
    res= list()

    for i in Element:
       ret= Task(i)

       if(ret == True):
           res.append(i)
    return res

def main():

    numbers = list(map(int, input("Enter number").split()))
    print(numbers)

    Data = list(filterx(FilterData,numbers))
    print(Data)

    Increment = list(map(IncrementBy10,Data))
    print(Increment)

    ProductValue = reduce(Product,Increment)
    print(ProductValue)

                   
if __name__ =="__main__":
    main()


