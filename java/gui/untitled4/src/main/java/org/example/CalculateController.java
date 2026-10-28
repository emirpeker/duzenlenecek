package org.example;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class CalculateController {

    @FXML
    private TextField display;

    private double number1 = 0;
    private String operator = "";
    private boolean startNewNumber = true;

    @FXML
    private void processNumbers(ActionEvent event) {
        if (startNewNumber) {
            display.setText("");
            startNewNumber = false;
        }
        String value = ((Button) event.getSource()).getText();
        display.setText(display.getText() + value);
    }

    @FXML
    private void processOperators(ActionEvent event) {
        String value = ((Button) event.getSource()).getText();

        if (!value.equals("=")) {
            if (!operator.isEmpty()) {
                return;
            }
            operator = value;
            number1 = Double.parseDouble(display.getText());
            display.setText("");
            startNewNumber = true;
        } else {
            if (operator.isEmpty()) {
                return;
            }
            double number2 = Double.parseDouble(display.getText());
            double output = calculate(number1, number2, operator);

            if (output % 1 == 0) {
                display.setText(String.valueOf((int) output));
            } else {
                display.setText(String.valueOf(output));
            }
            operator = "";
            startNewNumber = true;
        }
    }

    private double calculate(double num1, double num2, String op) {
        switch (op) {
            case "+": return num1 + num2;
            case "-": return num1 - num2;
            case "x": return num1 * num2;
            case "÷":
                if (num2 == 0) return 0;
                return num1 / num2;
            default: return 0;
        }
    }

    @FXML
    private void clear(ActionEvent event) {
        display.setText("");
        operator = "";
        startNewNumber = true;
        number1 = 0;
    }

    @FXML
    private void backspace(ActionEvent event) {
        String text = display.getText();
        if (text.length() > 0) {
            display.setText(text.substring(0, text.length() - 1));
        }
    }
}