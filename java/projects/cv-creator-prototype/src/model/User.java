package model;

public class User {
    private String name;
    private String email;
    private String summary;

    public User(String name, String email, String summary) {
        this.name = name;
        this.email = email;
        this.summary = summary;
    }

    // GETTER & SETTER’LAR
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getSummary() { return summary; }
    public void setSummary(String summary) { this.summary = summary; }
}
