a=0
for i in range(1,50) :
    s=str(i)
    l=int(len(s))
    for j in range(0,l):
     a=a+int(s[j])
    if a<9 :
     print(i) 
