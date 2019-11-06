for i in range(10,100):
    s=str(i)
    for j in range(10,100):
        d=str(j)
        if (int(s[0]+s[1]+d[0]+d[1])==11*(i+j)) :
            print(s,d)
