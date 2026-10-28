public class CreditCardPayment extends Payment {
    public CreditCardPayment(double amount) {
        super(amount);
    }
    @Override
    public double calculateDiscount() {
        return amount*0.05;
    }
}
