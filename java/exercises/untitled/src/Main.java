public class Main {
    public static void main(String[] args) {
        int sayi=12345;
        int mod=0;
        boolean var_mi=false;
        while(sayi>0){
            mod=sayi%10;
            if(mod==7){
                var_mi=true;
                break;
            }
            sayi=sayi/10;
        }
        if(var_mi==true){
            System.out.println("Sayının içinde 7 vardır!");
        }
        else{
            System.out.println("Sayının içinde 7 yoktur!");
        }
    }
}