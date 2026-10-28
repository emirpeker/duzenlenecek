import time
import calendar

def tarih_formatla(tarih_str):
    parca=tarih_str.split("-")
    if len(parca)!=3:
        return "Format yanlis!"
    gun,ay,yil=parca
    if not(gun.isdigit() and ay.isdigit() and yil.isdigit()):
        return "Sadece sayi girmeniz lazim!"
    gun=int(gun)
    ay=int(ay)
    yil=int(yil)
    if ay<1 or ay>12:
        return "Ay 1 ile 12 arasi olmalidir!"
    
    max_gun=calendar.monthrange(yil,ay)[1]
    if gun<1 or gun>max_gun:
        return "Gün gecerli degil!"
    
    format1=f"{gun:02d}/{ay:02d}/{yil}"
    format2=f"{yil}-{ay:02d}-{gun:02d}"

    return format1,format2

print(tarih_formatla("15-04-2024"))