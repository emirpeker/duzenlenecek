from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def alanHesapla(self):
        ...
    @abstractmethod
    def cevreHesapla(self):
        ...
class Circle(Shape):
    def __init__(self,yaricap):
        self.yaricap=yaricap
    def alanHesapla(self):
        return 3.14*self.yaricap*self.yaricap
    def cevreHesapla(self):
        return 3.14*2*self.yaricap
class Rectangle(Shape):
    def __init__(self,kisaKenar,uzunKenar):
        self.kisaKenar=kisaKenar
        self.uzunKenar=uzunKenar
    def alanHesapla(self):
        return self.kisaKenar*self.uzunKenar
    def cevreHesapla(self):
        return 2*(self.kisaKenar+self.uzunKenar)
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def cevreHesapla(self):
        return self.a+self.b+self.c
    def alanHesapla(self):
        s = (self.a + self.b + self.c) / 2
        alan = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return alan
    
daire = Circle(5)
dikdortgen = Rectangle(4, 6)
ucgen = Triangle(3,4,5) # 3-4-5 üçgeni

# Sonuçları yazdıralım
print(f"Daire Alanı: {daire.alanHesapla():.2f}, Çevresi: {daire.cevreHesapla():.2f}")
print(f"Dikdörtgen Alanı: {dikdortgen.alanHesapla()}, Çevresi: {dikdortgen.cevreHesapla()}")
print(f"Üçgen Alanı: {ucgen.alanHesapla()}, Çevresi: {ucgen.cevreHesapla()}")