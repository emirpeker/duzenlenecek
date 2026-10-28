import java.util.Scanner;
import java.util.InputMismatchException;

public class Main{
    public static void main(String[] args) {
        Ogrenci ogr1 = new Ogrenci();
        Scanner scanner = new Scanner(System.in);
        System.out.println("4 adet not giriniz.");

        for(int i=0;i<4;i++){
            System.out.print((i+1)+". notu giriniz: ");
            try{
                int girilenNot=scanner.nextInt();
                ogr1.notEkle(girilenNot);
            }
            catch(kucukDegerHatasi e){
                System.out.println("Hata: "+e.getHataliNot()+" not olarak eklenemez (0'dan küçük).");
            }
            catch(buyukDegerHatasi e){
                System.out.println("Hata: "+e.getHataliNot()+" not olarak eklenemez (100'den büyük).");
            }
            catch(InputMismatchException e){
                System.out.println("Hata: Sadece sayısal bir değer giriniz.");
                scanner.nextLine();
                i--;
            }
        }
        ogr1.notGoster();
        scanner.close();
    }
}