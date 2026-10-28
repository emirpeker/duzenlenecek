package controller;

import data.DataStore;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import model.Experience;

import java.net.URL;
import java.util.ResourceBundle;

public class ExperienceController implements Initializable {

    @FXML
    private TableView<Experience> tblExperience;

    @FXML
    private TableColumn<Experience, String> colCompany, colPosition, colStart, colEnd, colDesc;

    @FXML
    private TextField txtCompany, txtPosition, txtStart, txtEnd, txtDescription;

    private ObservableList<Experience> expList;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        expList = FXCollections.observableArrayList(DataStore.experienceList);

        colCompany.setCellValueFactory(v -> new javafx.beans.property.SimpleStringProperty(v.getValue().getCompany()));
        colPosition.setCellValueFactory(v -> new javafx.beans.property.SimpleStringProperty(v.getValue().getPosition()));
        colStart.setCellValueFactory(v -> new javafx.beans.property.SimpleStringProperty(v.getValue().getStartDate()));
        colEnd.setCellValueFactory(v -> new javafx.beans.property.SimpleStringProperty(v.getValue().getEndDate()));
        colDesc.setCellValueFactory(v -> new javafx.beans.property.SimpleStringProperty(v.getValue().getDescription()));

        tblExperience.setItems(expList);
    }

    @FXML
    private void addExperience() {
        if (txtCompany.getText().isEmpty() ||
                txtPosition.getText().isEmpty() ||
                txtStart.getText().isEmpty() ||
                txtEnd.getText().isEmpty() ||
                txtDescription.getText().isEmpty()) {

            showAlert("Hata", "Lütfen tüm alanları doldurun.");
            return;
        }

        Experience exp = new Experience(
                txtCompany.getText(),
                txtPosition.getText(),
                txtStart.getText(),
                txtEnd.getText(),
                txtDescription.getText()
        );

        expList.add(exp);
        DataStore.experienceList.add(exp);

        clearFields();
    }

    @FXML
    private void deleteExperience() {
        Experience selected = tblExperience.getSelectionModel().getSelectedItem();

        if (selected == null) {
            showAlert("Uyarı", "Lütfen silmek için bir kayıt seçin.");
            return;
        }

        expList.remove(selected);
        DataStore.experienceList.remove(selected);
    }

    private void clearFields() {
        txtCompany.clear();
        txtPosition.clear();
        txtStart.clear();
        txtEnd.clear();
        txtDescription.clear();
    }

    private void showAlert(String title, String msg) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(msg);
        alert.show();
    }
}
