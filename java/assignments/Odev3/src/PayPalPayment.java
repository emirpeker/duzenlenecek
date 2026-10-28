public class PayPalPayment extends Payment {
    public PayPalPayment(double amount) {
        super(amount);
    }
    @Override
    public double calculateDiscount() {
        return amount*0.03;
    }
}
