import random
a=random.randint(10,98)
sa=str(a)
x=0
while x!=a :
  dogruyer=0
  yanlisyer=0
  x=int(input("10 ile 98 arasında bir sayı giriniz:"))
  s=str(x)
  if 10<=x<=98:
     if  sa[0]==s[0] :
        dogruyer+=1
        
     if sa[1]==s[1]:
        dogruyer+=1
       
     if sa[0]==s[1]:
        yanlisyer-=1
        
     if sa[1]==s[0]:
         yanlisyer-=1
     print("doğru yer:",dogruyer)
     print("yanlis yer:",yanlisyer)
  else :
    print("10 ile 98 arasında dedik!")




    
print("TEBRİKS ")

    
