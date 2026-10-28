public abstract class Payment {
    protected double amount;
    public Payment(double amount) {
        this.amount = amount;
    }
    public abstract double calculateDiscount();
    public double calculateDiscount(String discountCode){
        double discountedAmount = amount-calculateDiscount();
        double extraDiscount=0.0;

        if(discountCode.equals("WELCOME10")){
            extraDiscount=discountedAmount*0.10;
        }
        else if(discountCode.equals("VIP")){
            extraDiscount=discountedAmount*0.15;
        }
        double totalDiscount=calculateDiscount()+extraDiscount;
        return amount-totalDiscount;
    }
    public double calculateDiscount(String discountCode,int loyaltyYears){
        double discountedAmount = calculateDiscount(discountCode);
        double extraDiscount=0.0;
        if(loyaltyYears>5){
            extraDiscount=discountedAmount*0.05;
        }
        return discountedAmount-extraDiscount;
    }

}
