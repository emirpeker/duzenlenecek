public class buyukDegerHatasi extends Exception{
    private int hataliNot;
    public buyukDegerHatasi(int hataliNot){
        super(hataliNot+" notu 100'den buyuk olamaz!");
        this.hataliNot=hataliNot;
    }
    public int getHataliNot(){
        return hataliNot;
    }
}
