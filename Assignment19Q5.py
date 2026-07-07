
MultiplyBy2 = lambda x: x*2

MaxNumber = lambda x,y : x if x>y else y


def PrimeNumber(Numbers):
    primmelist= list()
  

    if(Numbers > 1):
        for p in range(2,int(Numbers/2)+1):
            if(Numbers%p) == 0:
                    break
        else: 
            primmelist.append(Numbers)
       
        
    return primmelist   

 
def mapx(Task,Number):
    ret= list()

    for i in Number:
        no = Task(i)
        ret.append(no)
    return ret     

def reducex(Task,Number):
    sum= 0

    for i in Number:
        no= Task(sum,i)

    return no    

                

def main():
    numbers= list(map(int,input("Enter Number of elements").split()))

    Data= list(filter(PrimeNumber,numbers)) 
    print("Data--",Data)

    MultiData = list(mapx(MultiplyBy2,Data))
    print("Map Data--",MultiData)

    MaxData= reducex(MaxNumber,MultiData)
    print("Max Number",MaxData)


if __name__ =="__main__":
    main()