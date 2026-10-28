import random
import string

def sifreUret(uzunluk):
    buyukHarf=string.ascii_uppercase
    kucukHarf=string.ascii_lowercase
    rakam=string.digits
    ozel=string.punctuation
    
    if uzunluk<4:
        return "Sifre en az 4 karakter olmalidir!"
    sifre=[]
    sifre.append(random.choice(buyukHarf))
    sifre.append(random.choice(kucukHarf))
    sifre.append(random.choice(rakam))
    sifre.append(random.choice(ozel))
    
    tumKarakterler=buyukHarf+kucukHarf+rakam+ozel
    
    for i in range(uzunluk - 4):
        sifre.append(random.choice(tumKarakterler))
        
    random.shuffle(sifre)
    return "".join(sifre)

sifreUzunluk=input("Oluşturulacak şifrenin uzunluğunu girin (Örn: 12): ")

if sifreUzunluk.isdigit():
    istenenUzunluk =int(sifreUzunluk)
    
    yeniSifre=sifreUret(istenenUzunluk)
    print(f"\nOluşturulan {istenenUzunluk} karakterli şifreniz: {yeniSifre}")
else:
    print("Hata:Lütfen geçerli bir sayi girin.")