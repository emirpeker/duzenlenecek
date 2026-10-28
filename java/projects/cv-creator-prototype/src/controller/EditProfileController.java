package controller;

import data.DataStore;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import model.User;

import java.net.URL;
import java.util.ResourceBundle;

public class EditProfileController implements Initializable {

    @FXML
    private TextField txtName;

    @FXML
    private TextField txtEmail;

    @FXML
    private TextArea txtSummary;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        // Mevcut kullanıcı bilgilerini alanlara yükle
        User u = DataStore.loggedUser;

        txtName.setText(u.getName());
        txtEmail.setText(u.getEmail());
        txtSummary.setText(u.getSummary());
    }

    @FXML
    private void saveProfile() {

        // Alanları oku
        String name = txtName.getText();
        String email = txtEmail.getText();
        String summary = txtSummary.getText();

        if (name.isEmpty() || email.isEmpty() || summary.isEmpty()) {
            showAlert("Hata", "Lütfen tüm alanları doldurun.");
            return;
        }

        // Kullanıcıyı güncelle
        DataStore.loggedUser.setName(name);
        DataStore.loggedUser.setEmail(email);
        DataStore.loggedUser.setSummary(summary);

        showAlert("Başarılı", "Profil başarıyla güncellendi.");
    }

    private void showAlert(String title, String msg) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(msg);
        alert.show();
    }
}
