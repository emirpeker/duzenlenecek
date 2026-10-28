class Kullanici{
    private String ad;
    private String soyad;
    private MuzikKoleksiyonu kolesikyon;

    public Kullanici(String ad, String soyad){
        this.ad = ad;
        this.soyad = soyad;
        this.kolesikyon = new MuzikKoleksiyonu();
    }
    public void Sarki_ekle(Sarki sarki){
        kolesikyon.sarkiEkle(sarki);
    }
    public void Sarki_kaldir(String ad){
        kolesikyon.sarkiKaldir(ad);
    }
    public void Sarki_ara(String ad){
        kolesikyon.sarkiAra(ad);
    }
    public void Sarki_listele(){
        System.out.println("\nKullanici: "+ad+" "+soyad);
        kolesikyon.listele();
    }
}