package controller;

import data.DataStore;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.control.Label;
import model.User;

import java.net.URL;
import java.util.ResourceBundle;

public class ProfileController implements Initializable {

    @FXML
    private Label lblName;

    @FXML
    private Label lblEmail;

    @FXML
    private Label lblSummary;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        User u = DataStore.loggedUser;

        lblName.setText("Ad Soyad: " + u.getName());
        lblEmail.setText("Email: " + u.getEmail());
        lblSummary.setText("Özet: " + u.getSummary());
    }
    @FXML
    private void editProfile() {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("/view/edit_profile.fxml"));
            DashboardController.changeContent(root);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


}
