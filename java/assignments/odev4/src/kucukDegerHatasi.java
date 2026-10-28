public class kucukDegerHatasi extends Exception{
    private int hataliNot;
    public kucukDegerHatasi(int hataliNot){
        super(hataliNot+" notu 0'dan kucuk olamaz!");
        this.hataliNot=hataliNot;
    }
    public int getHataliNot(){
        return hataliNot;
    }
}
