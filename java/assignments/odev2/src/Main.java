import java.util.ArrayList;
class Sarki{
    private String ad;
    private String sanatci;
    private String album;
    private int sure;

    public Sarki(String ad, String sanatci, String album, int sure) {
        this.ad = ad;
        this.sanatci = sanatci;
        this.album = album;
        this.sure = sure;
    }
    public String getAd() {return ad;}
    public int getSure() {return sure;}

    @Override
    public String toString() {
        return ad+" - "+sanatci+" ( "+album+" ) | "+sure+" dk";
    }
}
class MuzikKolesikyonu{
    private ArrayList<Sarki> sarkilar;
    public MuzikKolesikyonu() {
        sarkilar = new ArrayList<>();
    }
    public void ekle(Sarki sarki){
        sarkilar.add(sarki);
        System.out.println("Sarki eklendi! -->"+sarki.getAd());
    }
    public void kaldir(String ad){
        for(Sarki sarki : sarkilar) {
            if(sarki.getAd().equals(ad)){
                sarkilar.remove(sarki);
                System.out.println("Sarki silindi! -->"+ad);
                return;
            }
        }
        System.out.println("Sarki bulunamadi! "+ad);
    }
    public void ara(String ad){
        for(Sarki sarki:sarkilar){
            if(sarki.getAd().equals(ad)){
                System.out.println("Sarki bulundu! -->"+sarki);
                return;
            }
        }
        System.out.println("Sarki bulunamadi! "+ad);
    }
    public void listele(){
        System.out.println("\nSarki Listesi:");
        for(Sarki sarki:sarkilar){
            System.out.println("* "+sarki);
        }
        System.out.println("Toplam süre: "+toplam_sure()+"dk\n");
    }
    public int toplam_sure(){
        int toplam=0;
        for(Sarki sarki:sarkilar){
            toplam+=sarki.getSure();
        }
        return toplam;
    }
}
class Kullanici{
    private String ad;
    private String soyad;
    private MuzikKolesikyonu kolesikyon;

    public Kullanici(String ad, String soyad){
        this.ad = ad;
        this.soyad = soyad;
        this.kolesikyon = new MuzikKolesikyonu();
    }
    public void Sarki_ekle(Sarki sarki){
        kolesikyon.ekle(sarki);
    }
    public void Sarki_kaldir(String ad){
        kolesikyon.kaldir(ad);
    }
    public void Sarki_ara(String ad){
        kolesikyon.ara(ad);
    }
    public void Sarki_listele(){
        System.out.println("\nKullanici: "+ad+" "+soyad);
        kolesikyon.listele();
    }
}

public class    Main {
    public static void main(String[] args) {
        Kullanici kullanici=new Kullanici("Emir","Peker");

        Sarki sarki1=new Sarki("Let It Happen","Tame Impala","Currents",7);
        Sarki sarki2=new Sarki("We Are The People","Empire Of The Sun","Walking On A Dream",4);
        Sarki sarki3=new Sarki("Sorma","Sezen Aksu","Yürüyorum Düş Bahçeleri'nde..",4);

        kullanici.Sarki_ekle(sarki1);
        kullanici.Sarki_ekle(sarki2);
        kullanici.Sarki_ekle(sarki3);

        kullanici.Sarki_listele();
        kullanici.Sarki_ara("We Are The People");
        kullanici.Sarki_kaldir("Sorma");

        kullanici.Sarki_listele();
    }
}