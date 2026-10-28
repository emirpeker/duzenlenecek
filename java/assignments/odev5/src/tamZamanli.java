public class tamZamanli extends Calisan{
    private double aylikMaas;
    public tamZamanli(String isim,int Id,double aylikMaas){
        super(isim,Id);
        this.aylikMaas=aylikMaas;
    }
    @Override
    public double maasHesapla() {
        return this.aylikMaas;
    }
}
