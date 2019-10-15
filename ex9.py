#1 ile 999 arasında rakamları toplamı 9 dan küçük sayıları yan yana yazdıran program
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i+j+k<9 :
                a=100*i+10*j+k
                print(a,end=" ")
             
