import threading
def SumOfElements(Numbers,shared_storage):
    sum=0

    for i in Numbers:
        sum= sum+i

    shared_storage["sum_result"]=sum  

def ProductOfElements(Numbers,shared_storage):
    product=1

    for i in Numbers:
        product= product*i

    shared_storage["product_result"]=product       

def main():
    result= {}
    numbers= list(map(int,input("Enter list").split()))  
    t1= threading.Thread(target=SumOfElements,args=(numbers,result)) 
    t2= threading.Thread(target=ProductOfElements,args=(numbers,result)) 

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    sum_output= result.get("sum_result")
    print("Sum output",sum_output)

    product_output= result.get("product_result")
    print("Product output",product_output)



if __name__ == "__main__":
    main()    