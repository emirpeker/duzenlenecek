package org.example;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class CounterController {

    @FXML
    private TextField counterField;

    private int counter = 0;

    @FXML
    public void initialize() {
        counterField.setText(String.valueOf(counter));
    }

    @FXML
    protected void onCountUp() {
        counter++;
        counterField.setText(String.valueOf(counter));
    }

    @FXML
    protected void onCountDown() {
        counter--;
        counterField.setText(String.valueOf(counter));
    }

    @FXML
    protected void onReset() {
        counter = 0;
        counterField.setText(String.valueOf(counter));
    }
}
