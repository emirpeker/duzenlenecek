package controller;

import com.lowagie.text.Document;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
import data.DataStore;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import model.Education;
import model.Experience;
import model.Skill;
import model.User;

import java.io.FileOutputStream;

public class PdfController {

    @FXML
    private void generatePdf() {

        try {
            User u = DataStore.loggedUser;

            Document doc = new Document();
            PdfWriter.getInstance(doc, new FileOutputStream("cv_output.pdf"));
            doc.open();

            // ==== PROFIL BILGILERI ====
            doc.add(new Paragraph("=== PROFIL BILGILERI ==="));
            doc.add(new Paragraph("Ad Soyad: " + u.getName()));
            doc.add(new Paragraph("Email: " + u.getEmail()));
            doc.add(new Paragraph("Özet: " + u.getSummary()));
            doc.add(new Paragraph("\n"));


            // ==== EGITIMLER ====
            doc.add(new Paragraph("=== EGITIM BILGILERI ==="));
            for (Education e : DataStore.educationList) {
                doc.add(new Paragraph(e.getSchool() + " - " + e.getDepartment() +
                        " (" + e.getStartYear() + " - " + e.getEndYear() + ")"));
            }
            doc.add(new Paragraph("\n"));


            // ==== DENEYIM ====
            doc.add(new Paragraph("=== DENEYIM ==="));
            for (Experience ex : DataStore.experienceList) {
                doc.add(new Paragraph(ex.getCompany() + " / " + ex.getPosition() +
                        " (" + ex.getStartDate() + " - " + ex.getEndDate() + ")"));
            }
            doc.add(new Paragraph("\n"));


            // ==== YETENEKLER ====
            doc.add(new Paragraph("=== YETENEKLER ==="));
            for (Skill s : DataStore.skillList) {
                doc.add(new Paragraph("- " + s.getSkillName()));
            }

            doc.close();

            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("PDF Oluşturuldu");
            alert.setHeaderText(null);
            alert.setContentText("PDF başarıyla oluşturuldu!\nDosya: cv_output.pdf");
            alert.show();

        } catch (Exception e) {
            e.printStackTrace();

            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Hata");
            alert.setHeaderText(null);
            alert.setContentText("PDF oluşturulurken bir hata oldu!");
            alert.show();
        }

    }
}
