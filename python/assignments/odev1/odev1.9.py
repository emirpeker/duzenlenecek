sayi=int(input("Iki basamakli bir sayi gir: "))
if 9<sayi<100:
    onlarb=sayi//10
    birlerb=sayi%10
    toplam=onlarb+birlerb
    print("Girilen sayinin rakamlari toplami: ",toplam)
else:
    print("Hatali İslem!")