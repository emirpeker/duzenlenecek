public class DortIslem {
    public int Add(int a,int b)
    {
        return a+b;
    }
    public int Minus(int a,int b)
    {
        return a-b;
    }
    public int Multiply(int a,int b)
    {
        return a*b;
    }
    public float Divide(int a,int b)
    {
        if(b==0){
            System.out.println("Bölen 0 olamaz!");
            return Float.NaN;
        }
        else
        {
            return a/(float)b;
        }
    }
}
