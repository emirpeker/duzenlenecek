from datetime import datetime, timedelta

def hafta_gun_sayisi(baslangic,bitis):
    bas=datetime.strptime(baslangic,"%Y-%m-%d")
    bit=datetime.strptime(bitis,"%Y-%m-%d")

    haftalar=[]
    mevcut=bas
    while mevcut<=bit:
        hafta_basi=mevcut
        hafta_sonu=mevcut+timedelta(days=6)
        if hafta_sonu>bit:
            hafta_sonu=bit
        gun_sayisi=(hafta_sonu-hafta_basi).days+1
        haftalar.append(gun_sayisi)
        mevcut=hafta_sonu+timedelta(days=1)
    return haftalar

sonuc=hafta_gun_sayisi("2024-01-01","2024-12-31")
print("Toplam hafta sayisi:",len(sonuc))
print("Her haftadaki gun sayilari:",sonuc)