isim=str(input("Isminizi giriniz: "))
vize1=int(input("1.Vize sonucunuzu girin: "))
vize2=int(input("2.Vize sonucunuzu girin: "))
final=int(input("Final sonucunuzu girin: "))

ortalama=(vize1*0.2)+(vize2*0.2)+(final*0.6)
print(ortalama)

if ortalama<=30:
    print("Kaldi!")
elif ortalama==31 or ortalama==69:
    print("Kritik!")
elif ortalama>70:
    print("Gecti!")