public class Employee {
    private String name;
    int salary;
    private int workingHours;
    private int hireYear;

    public Employee(String name, int salary, int workingHours, int hireYear) {
        this.name = name;
        this.salary = salary;
        this.workingHours = workingHours;
        this.hireYear = hireYear;
    }

    // Metot adı küçük harfle başladı (Java standardı)
    public int tax() {
        if (this.salary > 1000) {
            // 'salary' değişkenini değiştirmek yerine,
            // sadece hesaplanan vergi miktarını döndür.
            return (int) (this.salary * 0.03);
        }
        // Maaş 1000'den azsa vergi 0'dır.
        return 0;
    }

    // Metot adı küçük harfle başladı
    public int bonus() {
        int extraHours = this.workingHours - 40;
        if (extraHours > 0) {
            return 30 * extraHours;
        }
        return 0;
    }

    // Metot adı küçük harfle başladı
    public int raiseSalary() {
        int workYear = 2020 - this.hireYear;

        // 'salary' değişkenini değiştirmek yerine,
        // sadece hesaplanan zam miktarını döndür.
        if (workYear < 10) {
            return (int) (this.salary * 0.05);
        } else if (workYear > 9 && workYear < 20) {
            return (int) (this.salary * 0.1);
        } else if (workYear >= 20) {
            return (int) (this.salary * 0.15);
        }

        // Eğer hiçbir koşul sağlanmazsa (örn: 2020 sonrası işe giriş)
        return 0;
    }

    @Override
    public String toString() {
        // Bu metodu da doldurmak isteyebilirsiniz.
        return "Employee{" +
                "name='" + name + '\'' +
                ", salary=" + salary +
                '}';
    }
}