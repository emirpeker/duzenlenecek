public class Main{
    public static void main(String[] args){
        Musteri musteri1= new Musteri();
        Musteri musteri2= new Musteri();

        musteri1=musteri2;

        musteri1.Add();
        musteri1.Update();
        musteri1.Remove();
    }
}

