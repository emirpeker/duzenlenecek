interface Cizilebilir{
    void ciz();
}
abstract class Sekil{
    String renk;
    Sekil(String renk){
        this.renk = renk;
    }
    abstract double alanHesapla();
    abstract double cevreHesapla();

    void bilgiGoster(){
        System.out.println("Renk: "+renk);
    }
}
class EskenarUcgen extends Sekil implements Cizilebilir {
    double kenar;
    EskenarUcgen(String renk,double kenar){
        super(renk);
        this.kenar = kenar;
    }
    @Override
    double alanHesapla() {
        return (Math.sqrt(3)/4)*kenar*kenar;
    }
    @Override
    double cevreHesapla() {
        return 3*kenar;
    }
    @Override
    public void ciz() {
        System.out.println("Eskenar ucgen ciziliyor.");
    }
}
class Dikdortgen extends Sekil implements Cizilebilir {
    double uzunKenar,kisaKenar;
    Dikdortgen(String renk,double kisaKenar,double uzunKenar){
        super(renk);
        this.kisaKenar = kisaKenar;
        this.uzunKenar = uzunKenar;
    }
    @Override
    double alanHesapla() {
        return uzunKenar*kisaKenar;
    }
    @Override
    double cevreHesapla() {
        return (uzunKenar+kisaKenar)*2;
    }
    @Override
    public void ciz() {
        System.out.println("Dikdortgen ciziliyor.");
    }
}
public class SekilTest{
    public static void main(String[] args) {
        Sekil ucgen=new EskenarUcgen("Mavi",5);
        ucgen.bilgiGoster();
        System.out.println("Alan: "+ucgen.alanHesapla());
        System.out.println("Cevre: "+ucgen.cevreHesapla());
        ((Cizilebilir)ucgen).ciz();

        Sekil dikdortgen=new Dikdortgen("Kırmızı",4,7);
        dikdortgen.bilgiGoster();
        System.out.println("Alan: "+dikdortgen.alanHesapla());
        System.out.println("Cevre: "+dikdortgen.cevreHesapla());
        ((Cizilebilir)dikdortgen).ciz();


    }
}