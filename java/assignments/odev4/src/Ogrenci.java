import java.util.ArrayList;

public class Ogrenci {
    private ArrayList<Integer> notlar=new ArrayList<>();
    public Ogrenci(){
        this.notlar=new ArrayList<>();
    }
    void notEkle(int puan)throws kucukDegerHatasi,buyukDegerHatasi{
        if(puan<0){
            throw new kucukDegerHatasi(puan);
        }
        if(puan>100){
            throw new buyukDegerHatasi(puan);
        }
        this.notlar.add(puan);
        System.out.println(puan+" notu eklendi!");
    }
    void notGoster(){
        System.out.print("Mevcut notlar: "+this.notlar.toString());
    }
}
