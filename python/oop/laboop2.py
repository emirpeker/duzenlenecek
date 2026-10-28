# while 1:
#     x=input("Bir sayi gir:")
#     if not x:
#         break
#     try:
#         y=1/float(x)
#     except ValueError:
#         print("Gecersiz sayi")
#         continue
#     except ZeroDivisionError:
#         print("Sifira bolum")
#         continue
#     break


def diziTopla(dizi):
    toplam=0
    try:
        for i in range(len(dizi)):
            toplam+=dizi[i]
    except ValueError:
            print("Sayi girin diziye")
    return toplam
dizi=[1,2,'c']
diziTopla(dizi)