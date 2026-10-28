package controller;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.layout.StackPane;

public class DashboardController {

    @FXML
    private StackPane contentArea;

    // Static referans (FXML ile işaretlenmez)
    private static StackPane staticContentArea;

    @FXML
    public void initialize() {
        staticContentArea = contentArea;  // Doğru şekilde atama
    }

    public static void changeContent(Parent page) {
        if (staticContentArea != null) {
            staticContentArea.getChildren().clear();
            staticContentArea.getChildren().add(page);
        } else {
            System.out.println("staticContentArea NULL – initialize() çalışmadı!");
        }
    }

    private void loadPage(String page) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("/view/" + page + ".fxml"));
            contentArea.getChildren().clear();
            contentArea.getChildren().add(root);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @FXML
    private void openProfile() {
        loadPage("profile");
    }

    @FXML
    private void openEducation() {
        loadPage("education");
    }

    @FXML
    private void openExperience() {
        loadPage("experience");
    }

    @FXML
    private void openSkills() {
        loadPage("skills");
    }

    @FXML
    private void openPdf() {
        loadPage("pdf");
    }
}
