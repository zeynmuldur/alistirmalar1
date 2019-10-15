#pisayisinin değerini buluyoruz
import math
toplam=0
for i in range(1,100000):
    toplam=toplam+1/pow(i,2)

pisayisi=pow(toplam*6,1/2)
print(pisayisi)
