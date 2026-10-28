public class serbest extends Calisan {
    private int projeSayisi;
    private int projeUcret;
    public serbest(String isim,int Id,int projeSayisi,int projeUcret) {
        super(isim,Id);
        this.projeSayisi = projeSayisi;
        this.projeUcret = projeUcret;
    }
    @Override
    public double maasHesapla(){
        return this.projeSayisi*this.projeUcret;
    }
}
