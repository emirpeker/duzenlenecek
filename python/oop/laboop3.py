class KucukDegerHatasi(Exception):
    """Girilen değer 0'dan küçük olduğunda fırlatılacak hata."""
    pass

class BuyukDegerHatasi(Exception):
    """Girilen değer 100'den büyük olduğunda fırlatılacak hata."""
    pass

ogrenci_notlari = []

def notEkle(puan):
    if puan < 0:
        raise KucukDegerHatasi(f"Hata: Girilen not ({puan}) 0'dan küçük olamaz!")
    
    elif puan > 100:
        raise BuyukDegerHatasi(f"Hata: Girilen not ({puan}) 100'den büyük olamaz!")
    
    else:
        ogrenci_notlari.append(puan)
        print(f"Başarılı: {puan} notu listeye eklendi.")

try:
    notEkle(50)
    notEkle(85)
    notEkle(105) 
    notEkle(-5)

except KucukDegerHatasi as e:
    print(e)
except BuyukDegerHatasi as e:
    print(e)

print("-" * 30)
print("Güncel Not Listesi:", ogrenci_notlari)