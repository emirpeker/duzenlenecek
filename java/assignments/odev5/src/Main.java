public class Main {
    public static void main(String[] args) {
        Calisan[] calisanlar=new Calisan[3];
        calisanlar[0]=new tamZamanli("Emir",1,10000);
        calisanlar[1]=new yariZamanli("Burak",2,50,25);
        calisanlar[2]=new serbest("Kuzey",3,5,1500);
        double toplamMaas=0.0;
        for(Calisan calisan:calisanlar){
            calisan.bilgiler();
            toplamMaas+=calisan.maasHesapla();
            System.out.println("-------");
        }
        System.out.println("\nAylik Toplam Maas Gideri: "+toplamMaas);
    }
}