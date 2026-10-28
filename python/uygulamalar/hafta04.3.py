def sifrepuan(sifreler):
    puanlar={}
    ozelkarakter=r"!@>£#$½{[]}\|-_!'^+%&/()=?_*-:;;,."
    for sifre in sifreler:
        puan=0
        if len(sifre)>=8:
            puan+=1
        if any(harf.isdigit() for harf in sifre):
            puan+=1
        if any(harf.isupper() for harf in sifre):
            puan+=1
        if any(harf in ozelkarakter for harf in sifre):
            puan+=1
        puanlar[sifre]=puan
    return puanlar 

sifreler=["1234","Password","Pass-2","PASSWORd-123"]
print(sifrepuan(sifreler))