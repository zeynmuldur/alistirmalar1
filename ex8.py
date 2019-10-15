for i in range(1,10) :
    for j in range (0,10):
        for k in range(0,10,2):
            if i==k or i==j or k==j or i==j==k:
                print(100*i+10*j+k)
