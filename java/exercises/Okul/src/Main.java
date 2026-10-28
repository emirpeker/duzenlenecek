public class Main {
    public static void main(String[] args) {
    OgrenciBilgileri ogrenciBilgileri=new OgrenciBilgileri();
    ogrenciBilgileri.setOgrenciAdi("Emir PEKER");
    ogrenciBilgileri.setOgrenciTc(12345);
    ogrenciBilgileri.setOgrenciYas(19);
    ogrenciBilgileri.setOgrenciNumarasi(1);

    System.out.println(ogrenciBilgileri.getOgrenciAdi());

    OgrenciIslemleri ogrenciIslemleri=new OgrenciIslemleri();
    ogrenciIslemleri.OgrenciEkle(ogrenciBilgileri);
    }
}