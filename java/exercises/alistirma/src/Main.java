import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        System.out.println("Sayı tahmin oyununa hos geldin!");
        System.out.println("1-100 arasi sayı gir: ");
        int tahmin =sc.nextInt();
        int sayi=rand.nextInt(101);
        while(tahmin!=sayi){
            if(tahmin<0 || tahmin>100){
                System.out.println("Geçersiz sayi");
                tahmin = sc.nextInt();
            } else if (tahmin<sayi) {
                System.out.println("Daha büyül");
                tahmin=sc.nextInt();
            }
            else{
                System.out.println("Daha kucuk");
                tahmin = sc.nextInt();
            }
        }System.out.println("tebirkler");
    }
}