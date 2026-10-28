public class Main {
    public static void main(String[] args) {
        int[] dizi = {1, 2, 3};
        System.out.println("Dizinin elemanları toplamı= " + topla(dizi, 3));
    }
    static int topla(int[] dizi, int boyut) {
        int toplam=0;
        try {
            for(int i=0;i<boyut;i++){
                toplam+=dizi[i];
            }
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Boyut hatasi!"+e);
        }
        catch (Exception e){
            System.out.println("Hata var"+e);
        }
        finally {
        System.out.println("Finisjed");
    }
        return toplam;
    }

}
