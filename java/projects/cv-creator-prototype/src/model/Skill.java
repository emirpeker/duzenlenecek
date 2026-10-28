package model;

public class Skill {
    private String skillName;
    private String level; // Beginner - Intermediate - Expert

    public Skill(String skillName, String level) {
        this.skillName = skillName;
        this.level = level;
    }

    // GETTER - SETTER
    public String getSkillName() {return skillName;}
    public void setSkillName(String skillName) {this.skillName = skillName;}

    public String getLevel() {return level;}
    public void setLevel(String level) {this.level = level;}
}
