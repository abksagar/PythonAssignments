
def ChkPrime(Number):
    if Number <=1 :
         return False
  
    for p in range(2,int(Number/2)+1):
         if Number % p == 0:
              return False
    return True
         
         
                


      