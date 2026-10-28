import javax.annotation.processing.SupportedSourceVersion;
import java.util.*;
public class Main {
    public static void main(String[] args) {
   /* int sayi1;
    Scanner input = new Scanner(System.in);
    System.out.println("1.Sayiyi gir: ");
    sayi1 = input.nextInt();
    System.out.println("2.Sayiyi gir: ");
    int sayi2 = input.nextInt();
    System.out.println("3.Sayiyi gir: ");
    int sayi3 = input.nextInt();
    if(sayi1<sayi2 && sayi2<sayi3){
        System.out.println("En büyük sayi: "+sayi3);
    }
    else if(sayi1>sayi2 && sayi2>sayi3){
        System.out.println("En büyük sayi: "+sayi1);
    }
    else{
        System.out.println("En büyük sayi: "+sayi2);
    }*/
    /*char grade='A';
    switch(grade){
        case 'A':
            System.out.println("Mükemmel : Gectiniz");
            break;
        case 'B':
            System.out.println("Çok Güzel : Geçtiniz");
            break;
        case 'C':
            System.out.println("İyi : Geçtiniz");
            break;
        case 'D':
            System.out.println("Fena Değil : Geçtiniz");
            break;
        case 'F':
            System.out.println("Kötü : Kaldınız");
            break;
        default:
            System.out.println("Geçersiz not girdiniz!");
    }*/
    /*
    String[] ogrenciler= new String[3];
    ogrenciler[0]="Engin";
    ogrenciler[1]="Demet";
    ogrenciler[2]="Mustafa";

    for(int i=0;i<ogrenciler.length;i++){
        System.out.println(ogrenciler[i]);
    }
    */
        /*
    double[] myList= new double[3];
    myList[0]=1.0;
    myList[1]=2.0;
    myList[2]=3.0;
    double max=myList[0];
    double total=0.0;
    for(double number:myList){
        total+=number;
        if(number>max){
            max=number;
        }
            System.out.println(number);
    }
    System.out.println(total);
    System.out.println(max);
    }

         */
       /*
        String[][] sehirler = new String[3][3];
        sehirler[0][0] = "Istanbul";
        sehirler[0][1] = "Bursa";
        sehirler[0][2] = "Kocaeli";
        sehirler[1][0] = "Ankara";
        sehirler[1][1] = "Sivas";
        sehirler[1][2] = "Konya";
        sehirler[2][0] = "İzmir";
        sehirler[2][1] = "Muğla";
        sehirler[2][2] = "Aydın";

        for(int i=0;i<3;i++) {
            System.out.println("-------------");
            for(int j=0;j<3;j++) {
                System.out.println(sehirler[i][j]+" ");
            }
        }
    }
    */
        String mesaj = "Bugun hava cok guzel!";
        System.out.println(mesaj);
        System.out.println("5.eleman: " + mesaj.charAt(4));
        System.out.println(mesaj.concat(" Yaşasın!"));
        System.out.println(mesaj.startsWith("B"));
        System.out.println(mesaj.endsWith("!"));
        char[] karakterler = new char[5];
        mesaj.getChars(0, 5, karakterler, 0);
        System.out.println(karakterler);
        System.out.println(mesaj.indexOf('a'));
        System.out.println(mesaj.replace('a', 'z'));
        System.out.println(mesaj.substring(2));
        for(String kelime:mesaj.split(" ")){
            System.out.println(kelime);
        }

    }
}