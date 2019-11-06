x=input("3 ya da 4 basamaklı bir sayı giriniz:")
s=str(x)
if len(s)==3:
    if s[0]==s[2]:
        print("girdiğiniz sayı palindromiktir.")
    else:
        print("girdiğiniz sayı palindromik değildir.")
elif len(s)==4:
    if s[0]==s[3] and s[1]==s[2] :
        print("girdiğiniz sayı palindromiktir.")
    else:
        print("girdiğiniz sayı palindromik değildir.")
else:
    print("3 ya da 4 basamaklı bir sayı girin!")
