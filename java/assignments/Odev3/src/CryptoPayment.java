public class CryptoPayment extends Payment {
    public CryptoPayment(double amount) {
        super(amount);
    }
    @Override
    public double calculateDiscount() {
        return amount*0.02;
    }
}
