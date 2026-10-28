package data;

import model.*;
import java.util.ArrayList;
import java.util.List;

public class DataStore {

    public static User loggedUser = null;

    public static List<Education> educationList = new ArrayList<>();
    public static List<Experience> experienceList = new ArrayList<>();
    public static List<Skill> skillList = new ArrayList<>();

    static {
        loggedUser = new User(
                "Test Kullanıcı",
                "test@example.com",
                "Kendini geliştiren bir yazılım geliştirici."
        );
    }

}
