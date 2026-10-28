package controller;

import data.DataStore;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import model.Education;

import java.net.URL;
import java.util.ResourceBundle;

public class EducationController implements Initializable {

    @FXML
    private TableView<Education> tblEducation;

    @FXML
    private TableColumn<Education, String> colSchool, colDepartment, colStart, colEnd;

    @FXML
    private TextField txtSchool, txtDepartment, txtStart, txtEnd;

    private ObservableList<Education> eduList;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Listeyi DataStore'dan al
        eduList = FXCollections.observableArrayList(DataStore.educationList);

        // Kolonları modele bağla
        colSchool.setCellValueFactory(cellData -> new javafx.beans.property.SimpleStringProperty(cellData.getValue().getSchool()));
        colDepartment.setCellValueFactory(cellData -> new javafx.beans.property.SimpleStringProperty(cellData.getValue().getDepartment()));
        colStart.setCellValueFactory(cellData -> new javafx.beans.property.SimpleStringProperty(cellData.getValue().getStartYear()));
        colEnd.setCellValueFactory(cellData -> new javafx.beans.property.SimpleStringProperty(cellData.getValue().getEndYear()));

        // TableView doldur
        tblEducation.setItems(eduList);
        System.out.println("Edu açıldı!");
    }

    @FXML
    private void addEducation() {
        String school = txtSchool.getText();
        String department = txtDepartment.getText();
        String start = txtStart.getText();
        String end = txtEnd.getText();

        if (school.isEmpty() || department.isEmpty() || start.isEmpty() || end.isEmpty()) {
            showAlert("Hata", "Tüm alanları doldurmalısınız.");
            return;
        }

        Education edu = new Education(school, department, start, end);
        eduList.add(edu);
        DataStore.educationList.add(edu);

        clearFields();
    }

    @FXML
    private void deleteEducation() {
        Education selected = tblEducation.getSelectionModel().getSelectedItem();
        if (selected == null) {
            showAlert("Uyarı", "Silmek için bir kayıt seçmelisiniz.");
            return;
        }

        eduList.remove(selected);
        DataStore.educationList.remove(selected);
    }

    private void clearFields() {
        txtSchool.clear();
        txtDepartment.clear();
        txtStart.clear();
        txtEnd.clear();
    }

    private void showAlert(String title, String msg) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(msg);
        alert.show();
    }
}
