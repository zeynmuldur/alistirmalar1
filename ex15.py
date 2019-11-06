import math
def asal(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n%i)==0 :
            return False
    return True

for j in range(10000,100000,1):
    if(asal(j)):
     print(j)
