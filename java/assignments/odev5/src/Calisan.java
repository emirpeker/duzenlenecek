public abstract class Calisan implements Imaas{
    private String isim;
    private int id;
    public Calisan(String isim,int id){
        this.isim = isim;
        this.id = id;
    }
    public String getIsim(){
        return isim;
    }
    public int getId(){
        return id;
    }
    @Override
    public abstract double maasHesapla();
    @Override
    public void bilgiler(){
        System.out.println("Calisan tipi: "+this.getClass().getSimpleName());
        System.out.println("Id: "+this.getId());
        System.out.println("Isim: "+this.getIsim());
        System.out.println("Hesaplanan Aylik Maas: "+this.maasHesapla());
    }
}
