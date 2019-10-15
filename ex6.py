sayac=0
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
         for l in range(0,10):
           if i>l :
               print(i*1000+j*100+k*10+l)
               sayac+=1

print("su kadar sayı var:",sayac)
    
            
