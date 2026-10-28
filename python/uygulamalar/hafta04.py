import math
def kare():
    kisa=int(input("Kisa kenari gir: "))
    uzun=int(input("Uzun kenari gir: "))
    alan=kisa*uzun
    cevre=(kisa+uzun)*2
    print("Alan:",alan," Cevre",cevre)
def cember():
    yaricap=int(input("Yaricapi gir:"))
    alan=math.pi*yaricap*yaricap
    cevre=2*math.pi*yaricap
    print("Alan:",alan," Cevre:",cevre)
def sec():
    secim=input("Kare mi Çember mi sececeksin(Kare için KARE, Çember için CEMBER)\n")
    if(secim=="KARE"):
        kare()
    elif secim=="CEMBER":
        cember()
    else:
        print("Hatali islem!")
sec()