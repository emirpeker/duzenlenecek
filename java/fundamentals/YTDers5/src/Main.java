public class Main{
    public static void main(String[] args){
        Product product = new Product(1,"Laptop","Asus Laptop",3000,2,"siyah");
        /*product.set_name("Laptop");
        product.set_description("Asus Laptop");
        product.set_price(5000);
        product.setId(1);
        product.set_stockAmount(3);
        product.getId();*/

        productManager ProductManager=new productManager();
        ProductManager.Add(product);
        ProductManager.Add2(1," ","",200,2);
        System.out.println(product.get_name());
    }
}