package controller;

import data.DataStore;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import model.Skill;

import java.net.URL;
import java.util.ResourceBundle;

public class SkillsController implements Initializable {

    @FXML
    private TableView<Skill> tblSkills;

    @FXML
    private TableColumn<Skill, String> colSkill, colLevel;

    @FXML
    private TextField txtSkill;

    @FXML
    private ComboBox<String> cmbLevel;

    private ObservableList<Skill> skillList;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        skillList = FXCollections.observableArrayList(DataStore.skillList);

        // ComboBox seviyeleri
        cmbLevel.setItems(FXCollections.observableArrayList(
                "Beginner", "Intermediate", "Expert"
        ));

        // Kolon bağlamaları
        colSkill.setCellValueFactory(v ->
                new javafx.beans.property.SimpleStringProperty(v.getValue().getSkillName())
        );
        colLevel.setCellValueFactory(v ->
                new javafx.beans.property.SimpleStringProperty(v.getValue().getLevel())
        );

        tblSkills.setItems(skillList);
    }

    @FXML
    private void addSkill() {
        String skillName = txtSkill.getText();
        String level = cmbLevel.getValue();

        if (skillName == null || skillName.isEmpty() || level == null) {
            showAlert("Hata", "Lütfen tüm alanları doldurun.");
            return;
        }

        Skill skill = new Skill(skillName, level);
        skillList.add(skill);
        DataStore.skillList.add(skill);

        txtSkill.clear();
        cmbLevel.setValue(null);
    }

    @FXML
    private void deleteSkill() {
        Skill selected = tblSkills.getSelectionModel().getSelectedItem();

        if (selected == null) {
            showAlert("Uyarı", "Silmek için bir yetenek seçmelisiniz.");
            return;
        }

        skillList.remove(selected);
        DataStore.skillList.remove(selected);
    }

    private void showAlert(String title, String msg) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setContentText(msg);
        alert.show();
    }
}
