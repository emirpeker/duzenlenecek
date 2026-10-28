package model;

public class Education {
    private String school;
    private String department;
    private String startYear;
    private String endYear;

    public Education(String school, String department, String startYear, String endYear) {
        this.school = school;
        this.department = department;
        this.startYear = startYear;
        this.endYear = endYear;
    }

    // GETTER - SETTER
    public String getSchool() {return school;}
    public void setSchool(String school) {this.school = school;}

    public String getDepartment() {return department;}
    public void setDepartment(String department) {this.department = department;}

    public String getStartYear() {return startYear;}
    public void setStartYear(String startYear) {this.startYear = startYear;}

    public String getEndYear() {return endYear;}
    public void setEndYear(String endYear) {this.endYear = endYear;}
}
