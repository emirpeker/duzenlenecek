import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Employee emp1=new Employee("Kemal",2000,45,1985);
        System.out.println("Tax: "+emp1.tax());
        System.out.println("Bonus: "+emp1.bonus());
        System.out.println("Raise: "+emp1.raiseSalary());
        double totalsalary=emp1.salary+emp1.bonus()+emp1.raiseSalary()-emp1.tax();
        System.out.println("totalSalary: "+totalsalary);
    }
}