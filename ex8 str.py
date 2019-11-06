sayac=0
for i in range(100,1000,2):
    s=str(i)
    if s[0]==s[1] or s[1]==s[2] or s[0]==s[1] or s[0]==s[1]==s[2]  :
        print(i)
        sayac+=1
print("3 basamaklı çift sayılarda en az 2 rakamı eşit olan",sayac,"tane sayı var.")
