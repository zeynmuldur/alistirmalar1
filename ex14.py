min=121212
for i in range(2,121212) :
    if (121212%i==0) :
        j=121212/i
        if(abs(i-j)<min) :
             min=abs(i-j)
             a=i
             b=int(j)
print(a,b)
