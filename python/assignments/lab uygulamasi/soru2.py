kullanicilar={
    'Ali':{'yas':24,'sehir':'Ankara'},
    'Ayşe':{'yas':31,'sehir':'İstanbul'},
    'Mehmet':{'yas':45,'sehir':'İzmir'},
    'Emir':{'yas':19,'sehir':'Amasya'},
    'Nehir':{'yas':17,'sehir':'Edirne'},
}
def kullanici_grupla(kullanicilar):
    yasGrup={
        '18 ve Alti':[],
        '18-25 Arasi':[],
        '26-35 Arasi':[],
        '36 ve Ustu':[]
    }
    sehirGrup={}

    for isim,bilgiler in kullanicilar.items():
        yas=bilgiler['yas']
        sehir=bilgiler['sehir']
        if yas<=18:
            yasGrup['18 ve Alti'].append(isim)
        elif 18<yas<26:
            yasGrup['18-25 Arasi'].append(isim)
        elif 26<=yas<36:
            yasGrup['26-35 Arasi'].append(isim)
        elif yas>=36:
            yasGrup['36 ve Ustu'].append(isim)

        if sehir in sehirGrup:
            sehirGrup[sehir].append(isim)
        else:
            sehirGrup[sehir]=[isim]
    print("Yasa gore kullanicilar")
    for grup,kisiler in yasGrup.items():
        print(f"{grup}:{kisiler}")
    print("\nSehirlere gore kullanicilar")
    for sehir,kisiler in sehirGrup.items():
        print(f"{sehir}:{kisiler}")
kullanici_grupla(kullanicilar)