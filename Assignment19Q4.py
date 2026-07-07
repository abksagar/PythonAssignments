
EvenNumber= lambda x : x%2==0

Square = lambda x: x*x

Addition = lambda x,y : x+y



def filterx(Task,Number):

    evenList= list()

    for i in Number:
        ret= Task(i)

        if(ret == True):
            evenList.append(i)

    return evenList

def mapx(Task,Number):
    mapList= list()

    for i in Number:
        ret = Task(i)
        mapList.append(ret)

    return mapList

def reduceX(Task,Element):
    sum=0
    for i in Element:
        sum= Task(sum,i)

    return sum

def main():

    numbers= list(map(int,input("Enter list of numbers").split()))  

    FilterOutput= list(filter(EvenNumber,numbers))
    print(FilterOutput)

    SquareOutput= list(mapx(Square,FilterOutput))
    print(SquareOutput)

    Sum= reduceX(Addition,SquareOutput)
    print(Sum)

if __name__ =="__main__":
    main()
            

