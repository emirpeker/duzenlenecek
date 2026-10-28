public class Main {
    public static void main(String[] args) {
        /*int sayi=1;
        boolean check=true;
        if(sayi==1){
            System.out.println("Sayi asal degil");
            return;
        }
        if(sayi<2){
            System.out.println("Sayi geçersiz");
        }
        for(int i=2;i<sayi;i++){
            if(sayi%i==0){
                check=false;
                System.out.println("Sayi asal degil");
                break;
            }
        }
        if(check){
            System.out.println("Sayi asal");
        }*/
        int[] sayilar= new int[] {1,2,5,7,9,0};
        int aranacak=15;
        boolean kontrol=false;
        for(int i=0;i<sayilar.length;i++){
            if(sayilar[i]==aranacak){
                System.out.println("Sayi dizide vardır. Dizinin "+(i+1)+". elemanidir.");
                kontrol=true;
                break;
            }
        }
        if(kontrol==false){
            System.out.println("Sayi dizide bulunamadi.");
        }
    }
}