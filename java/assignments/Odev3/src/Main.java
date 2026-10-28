public class Main {
    public static void main(String[] args) {
        Payment[] payments = {new CreditCardPayment(1000),new PayPalPayment(1000),new CryptoPayment(1000)};
        for (Payment payment : payments) {
            System.out.println("--- " + payment.getClass().getSimpleName() + " ---");
            System.out.println("Temel İndirim: "+payment.calculateDiscount());
            System.out.println("WELCOME10 Kodlu İndirim: "+payment.calculateDiscount("WELCOME10"));
            System.out.println("VIP Kodlu ve 6 Yıllık Müşteri İndirimi: "+payment.calculateDiscount("VIP",6));
            System.out.println();
        }
    }
}