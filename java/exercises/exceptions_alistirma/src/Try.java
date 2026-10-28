import java.util.Scanner;

public class Try {
    public static void main(String[] args) {
        System.out.println("Program basladi");
        int a=0,b;
        Scanner scan=new Scanner(System.in);
        try{
            a=2/1;//hata yakaladık
            b=scan.nextInt();
        }
        catch(ArithmeticException e){
            System.out.println(e.getMessage());
        }
        catch(Exception e){//Exception tüm hataları kapsar.
            System.out.println(e.toString());
        }
        int[] arr=new int[3];
        try{
            arr[4]=10;// tryda hataları iç içe yazarsak ilk hangisini görürse onun hatasını gösterir.
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println(e.toString());
        }

        System.out.println("Program bitti");
    }
}
