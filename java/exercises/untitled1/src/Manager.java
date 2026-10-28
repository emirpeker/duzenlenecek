public class Manager extends Employee{
    private int num_of_employees;

    public Manager(String name,String department,int salary,int num_of_employees){
        super(name,department,salary);
        this.num_of_employees=num_of_employees;
    }
    public void riseSalary(int amount){
        System.out.println("Çalisanlara "+amount+" tl zam verildi!");
    }
    @Override
    public void showInfos(){
        super.showInfos();
        System.out.println("Sorumlu kişi sayisi: "+this.num_of_employees);
    }
}
