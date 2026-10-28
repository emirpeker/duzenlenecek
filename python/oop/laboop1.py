class Calisan:
    def __init__(self,name,lastname,salary,department):
        self.name=name
        self.lastname=lastname
        self.salary=salary
        self.department=department

    def bilgilerigetir(self):
        print("Personelin ismi: ",self.name)
        print(f"Soyisim: {self.lastname}")
        print(f"Maas: {self.salary}")
        print(f"Bolum: {self.department}")

    def maasArttir(self):
        self.salary=self.salary+1000
calisan1=Calisan("Emir","PEKER",20000,"CS")
calisan1.bilgilerigetir()
calisan1.maasArttir()
calisan1.bilgilerigetir()