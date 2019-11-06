def asalmi(i) :
    for j in range(2,i):
        if i%j==0 :
            return False
        else :
            return True


def superasalmi(i) :
    if i<=0 :
        return True
    elif asalmi(i) :
        return superasalmi(int(i/10))

for i in range(10000,100000) :
    if superasalmi(i) :
        print(i)
