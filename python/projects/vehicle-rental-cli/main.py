import sqlite3
from pathlib import Path
conn=sqlite3.connect(Path(__file__).with_name("tasitlar.db"))
cursor=conn.cursor()
print("Veritabani baglantisi basarili!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasitlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plaka TEXT UNIQUE,
    marka TEXT,
    model TEXT,
    ucret INTEGER,
    durum TEXT
)
""")
conn.commit()
print("\nTasitlar tablosu oluşturuldu.")

cursor.execute("""
CREATE TABLE IF NOT EXISTS kiralama_kayitlari (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plaka TEXT,
    musteri TEXT,
    baslangic TEXT,
    bitis TEXT,
    toplam_ucret INTEGER
)
""")
conn.commit()
print("\nKayit tablosu oluşturuldu.")

def arac_ekle(plaka,marka,model,ucret,durum="BOSTA"):
    cursor.execute("INSERT INTO tasitlar(plaka,marka,model,ucret,durum) VALUES(?,?,?,?,?)",(plaka,marka,model,ucret,durum))
    conn.commit()
    print("\nArac basariyla eklendi: ",plaka)

def araclari_listele():
    cursor.execute("SELECT * FROM tasitlar")
    sonuc = cursor.fetchall()

    if not sonuc:
        print("Tabloda araç yok.")
        return

    print("\n--- Araç Listesi ---")
    for id, plaka, marka, model, ucret, durum in sonuc:
        print(f"ID: {id} | Plaka: {plaka} | Marka: {marka} | Model: {model} | Ücret: {ucret} | Durum: {durum}")

def arac_sil(plaka):
    cursor.execute("DELETE FROM tasitlar WHERE plaka=?", (plaka,))
    conn.commit()
    print(f"{plaka} plakali arac silindi.")
arac_sil("34ABC494")

araclari_listele()

def kiralama_cakisiyor_mu(plaka, baslangic, bitis):
    cursor.execute("""
        SELECT 1
        FROM kiralama_kayitlari
        WHERE plaka = ?
          AND NOT (bitis <= ? OR baslangic >= ?)
        LIMIT 1
    """, (plaka, baslangic, bitis))

    return cursor.fetchone() is not None

import datetime

def arac_kirala(plaka, musteri, baslangic, bitis):
    # 1) Araç var mı, ucreti ne, durumu ne?
    cursor.execute("SELECT ucret, durum FROM tasitlar WHERE plaka=?", (plaka,))
    veri = cursor.fetchone()

    if veri is None:
        print("Araç bulunamadı!")
        return

    ucret, durum = veri

    if durum == "KİRALIK":
        print("Bu araç şu anda kirada (durum=KİRALIK).")
        # İstersen burada devam edip yine de tarih çakışmasına bakabilirsin
        # ama şimdilik direkt return yeterli.
        return

    # 2) Tarih formatları doğru mu? (yyyy-mm-dd bekliyoruz)
    try:
        bas = datetime.datetime.strptime(baslangic, "%Y-%m-%d")
        bit = datetime.datetime.strptime(bitis, "%Y-%m-%d")
    except ValueError:
        print("Tarih formatı hatalı! Örnek: 2025-01-15")
        return

    if bit <= bas:
        print("Bitiş tarihi, başlangıç tarihinden sonra olmalı!")
        return

    # 3) Aynı plakada tarih çakışması var mı?
    if kiralama_cakisiyor_mu(plaka, baslangic, bitis):
        print("Bu tarihler arasında bu araç için zaten kiralama kaydı var!")
        return

    # 4) Araç durumunu KİRALIK yap
    cursor.execute("UPDATE tasitlar SET durum='KİRALIK' WHERE plaka=?", (plaka,))
    conn.commit()

    # 5) Toplam gün ve ücret hesapla
    gun = (bit - bas).days
    toplam = gun * ucret

    # 6) Kiralama kaydını kaydet
    cursor.execute("""
        INSERT INTO kiralama_kayitlari (plaka, musteri, baslangic, bitis, toplam_ucret)
        VALUES (?, ?, ?, ?, ?)
    """, (plaka, musteri, baslangic, bitis, toplam))

    conn.commit()

    print(f"{plaka} plakalı araç {gun} gün için {musteri} adına kiralandı. Toplam: {toplam} TL")


# arac_ekle("34PLT007","BMW","E59",1500000,"KİRALİK")
# arac_ekle("34EMR206","SEAT","LEON",2350000,"BOSTA")
araclari_listele()

def arac_iade(plaka):
    cursor.execute("SELECT durum FROM tasitlar WHERE plaka=?",(plaka,))
    veri=cursor.fetchone()

    if veri is None:
        print("Arac bulunamadi!")
        return

    durum=veri[0]

    if durum == "BOSTA":
        print("Bu arac zaten bosta!")
        return

    cursor.execute("UPDATE tasitlar SET durum='BOSTA' WHERE plaka=?",(plaka,))
    conn.commit()
    print(f"{plaka} plakali arac iade edildi.")

arac_iade("34EMR206")
araclari_listele()

def arac_bul(plaka):
    cursor.execute("SELECT * FROM tasitlar WHERE plaka=?", (plaka,))
    return cursor.fetchone()
print(arac_bul("34PLT007"))

def bos_araclari_listele():
    cursor.execute("SELECT * FROM tasitlar WHERE durum='BOŞTA'")
    sonuc = cursor.fetchall()

    print("\n--- BOŞTA OLAN ARAÇLAR ---")
    if not sonuc:
        print("Boşta araç bulunamadı.")
        return

    for id, plaka, marka, model, ucret, durum in sonuc:
        print(f"{plaka} | {marka} {model} | Ücret: {ucret} | Durum: {durum}")

def kiralik_araclari_listele():
    cursor.execute("SELECT * FROM tasitlar WHERE durum='KİRALIK'")
    sonuc = cursor.fetchall()

    print("\n--- KİRALIK ARAÇLAR ---")
    if not sonuc:
        print("Kirada araç yok.")
        return

    for id, plaka, marka, model, ucret, durum in sonuc:
        print(f"{plaka} | {marka} {model} | Ücret: {ucret} | Durum: {durum}")

def marka_ara(marka):
    cursor.execute("SELECT * FROM tasitlar WHERE marka=?", (marka,))
    sonuc = cursor.fetchall()

    print(f"\n--- {marka} Markasına Ait Araçlar ---")
    if not sonuc:
        print(f"{marka} markasına ait araç yok.")
        return

    for id, plaka, model, marka, ucret, durum in sonuc:
        print(id, plaka, marka, model, ucret, durum)

def plaka_ara(plaka):
    cursor.execute("SELECT * FROM tasitlar WHERE plaka=?", (plaka,))
    sonuc = cursor.fetchone()

    print("\n--- Plaka Arama Sonucu ---")
    if sonuc is None:
        print(f"{plaka} plakalı araç bulunamadı.")
    else:
        print(sonuc)

def ucrete_gore_sirala(artan=True):
    if artan:
        cursor.execute("SELECT * FROM tasitlar ORDER BY ucret ASC")
        print("\n--- Ücreti Artan Sırada ---")
    else:
        cursor.execute("SELECT * FROM tasitlar ORDER BY ucret DESC")
        print("\n--- Ücreti Azalan Sırada ---")

    sonuc = cursor.fetchall()
    for row in sonuc:
        print(row)

def fiyat_araligi(min_fiyat, max_fiyat):
    cursor.execute("SELECT * FROM tasitlar WHERE ucret BETWEEN ? AND ?", (min_fiyat, max_fiyat))
    sonuc = cursor.fetchall()

    print(f"\n--- {min_fiyat} - {max_fiyat} Arası Araçlar ---")
    for row in sonuc:
        print(row)

def kiralama_kayitlari():
    cursor.execute("SELECT * FROM kiralama_kayitlari")
    sonuc = cursor.fetchall()

    print("\n--- Kiralama Kayıtları ---")
    for row in sonuc:
        print(row)
#arac_ekle("34ABC123", "Ford", "Focus", 3500)

arac_kirala("34MFS494", "Burak", "2025-08-01", "2025-08-05")
kiralama_kayitlari()