Urunler={"Telefon":2000,"Bilgisayar":5000,"Ucak":10000,"kalem":100,"Tablet":1000}
def al(aralikalt,aralikust):
    sonuc=[]
    for i,j in Urunler.items():
        if aralikalt<=j<=aralikust:
            sonuc.append(i)
    return sonuc

aralikalt=int(input("Verebileceginiz min tutar: "))
aralikust=int(input("Verebileceginiz max tutar: "))
print(al(aralikalt,aralikust))