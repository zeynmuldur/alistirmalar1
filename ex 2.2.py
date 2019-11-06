#1 den N e kadar olan sayilarin rekursif fonk ile toplanmasi
def toplam(i) :
    if i==1:
        return 1
    else :
        return i+toplam(i-1)
