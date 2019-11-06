import math
def asal(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n%i)==0 :
            return False
    return True

m=int(input("sayi girin:"))
if(m<2):
     print("1den büyük bir tam sayı gir!!!")
else:
     if(asal(m)):
         print("bu sayi asaldir!")
     else:
         print("asal degil:(")
