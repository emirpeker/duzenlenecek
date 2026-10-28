public class Ogrenci {
    private int ogrenciNumarasi;
    private String ogrenciAdi;
    private int ogrenciYas;

    public Ogrenci(){
        this.ogrenciNumarasi=0;
        this.ogrenciAdi="Bilinmiyor";
        this.ogrenciYas=0;
    }
    public Ogrenci(int ogrenciNumarasi, String ogrenciAdi, int ogrenciYas){
        this.ogrenciNumarasi=ogrenciNumarasi;
        this.ogrenciAdi=ogrenciAdi;
        this.ogrenciYas=ogrenciYas;
    }
    public int getOgrenciNumarasi() {
        return ogrenciNumarasi;
    }
    public String getOgrenciAdi(){
        return ogrenciAdi;
    }
    public int getOgrenciYas() {
        return ogrenciYas;
    }
    public void ogrenciBilgileriniYazdir(){
        System.out.println("Öğrenci Numarası: "+ogrenciNumarasi);
        System.out.println("Öğrenci Adi: "+ogrenciAdi);
        System.out.println("Öğrenci Yaşı: "+ogrenciYas);
    }
    public static void main(String[] args){
        Ogrenci ogrenci1=new Ogrenci();
        ogrenci1.ogrenciBilgileriniYazdir();

        Ogrenci ogrenci2=new Ogrenci(12345,"Ali Veli",20);
        ogrenci2.ogrenciBilgileriniYazdir();
    }
}
