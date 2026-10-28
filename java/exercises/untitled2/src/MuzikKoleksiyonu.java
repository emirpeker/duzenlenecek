import java.util.ArrayList;
public class MuzikKoleksiyonu {
    private ArrayList<Sarki> sarkilar;
    public MuzikKoleksiyonu() {
        sarkilar = new ArrayList<>();
    }
    public void sarkiEkle(Sarki sarki) {
        sarkilar.add(sarki);
        System.out.println("Sarki Eklendi--->"+sarki.getSarkiAdi());
    }
    public void sarkiKaldir(String sarkiAdi) {
        for (Sarki sarki : sarkilar) {
            if (sarki.getSarkiAdi().equals(sarkiAdi)) {
                sarkilar.remove(sarki);
                System.out.println("Sarki silindi--->"+sarkiAdi);
                return;
            }
        }
        System.out.println("Sarki bulunamadi!"+sarkiAdi);
    }
    public void sarkiAra(String sarkiAdi) {
        for (Sarki sarki : sarkilar) {
            if (sarki.getSarkiAdi().equals(sarkiAdi)) {
                System.out.println("Sarki bulundu--->"+sarkiAdi);
                return;
            }
        }
        System.out.println("Sarki bulunamadi!"+sarkiAdi);
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
