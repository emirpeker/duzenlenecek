public class yariZamanli extends Calisan {
    private double saatUcret;
    private int calisilanSaat;
    public yariZamanli(String isim,int Id,double saatUcret,int calisilanSaat){
    super(isim,Id);
    this.saatUcret=saatUcret;
    this.calisilanSaat=calisilanSaat;
    }
    @Override
    public double maasHesapla() {
        return this.saatUcret*this.calisilanSaat*4;
    }
}
