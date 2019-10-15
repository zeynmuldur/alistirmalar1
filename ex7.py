#ilk 2 rakamının toplamı üçüncü rakama eşit olan 3 basamaklı sayıları
#ve kaç tane olduklarını yazdıran program
sayac=0
for i in range(1,10):
    for j in range(0,10):
      for k in range(0,10):
         if i+j==k :
           print(i*100+j*10+k)
           sayac+=1
print("su kadar sayı var:",sayac)
