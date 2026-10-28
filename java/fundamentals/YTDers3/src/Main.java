public class Main {
    public static void main(String[] args) {
        //SayiBulmaca();
        String mesaj="Bugün hava güzel!";
        String yenimesaj = mesaj.substring(0,2);
        System.out.println(yenimesaj);
    }
    /*public static void SayiBulmaca() {
        int[]sayilar=new int[]{1,2,5,7,9,0};
        int aranacak=5;
        boolean varMi=false;
        for(int sayi : sayilar){
            if(sayi==aranacak){
                varMi=true;
                break;
            }
        }
        if(varMi){
            mesajVer(aranacak);
        }
        else{
            System.out.println("Sayi bulunamadi.");
        }
    }
    public static void mesajVer(int aranacak){
        System.out.println("Sayi mevcut."+aranacak);
    }*/
    public static void ekle(){
        System.out.println("Eklendi!");
    }
    public  static void sil(){
        System.out.println("Silindi!");
    }
    public static void guncelle(){
        System.out.println("Güncellendi!");
    }
}