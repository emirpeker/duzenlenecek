class Calisan():
    personel=[]
    def  __init__(self,isim):
        self.isim=isim
        self.kabiliyetleri=[]
        self.personele_ekle()
    def personel_sayisini_goruntule(self):
        print(len(self.personel))
    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adli kisi personele eklendi.'.format(self.isim))
    def personeli_goruntule(self):
        print('Personel listesi: ')
        for kisi in self.personel:
            print(kisi)
    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
    def kabiliyetleri_goruntule(self):
        print('{} adli kisinin kabiliyetleri: '.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)
