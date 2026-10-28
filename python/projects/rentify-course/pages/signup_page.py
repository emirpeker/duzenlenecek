from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt6 import uic
from pathlib import Path
import sys
import pages.car_page as car_page
from pages.main_window import MainWindow
from services.auth_service import register_user, is_valid_national_id, is_valid_email
from main import BASE_DIR


class SignupWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(BASE_DIR / "ui/signup.ui", self)

        self.btn_register.clicked.connect(self.register)
        try:
            self.lb_login.linkActivated.connect(self.open_login)
        except AttributeError:
            pass

    def register(self):
        username = self.le_username.text()
        email = self.le_email.text()
        name = self.le_name.text()
        last_name = self.le_last_name.text()
        national_id = self.le_id.text()
        password = self.le_password.text()
        confirm = self.le_password_confirm.text()

        if (
            not username
            or not email
            or not password
            or not name
            or not last_name
            or not national_id
        ):
            QMessageBox.warning(self, "Error", "All fields are required")
            return
        if not is_valid_email(email):
            QMessageBox.warning(
                self,
                "Invalid Email",
                "Please enter a valid email address",
            )
            return
        if not is_valid_national_id(national_id):
            QMessageBox.warning(
                self,
                "Invalid Identity Number",
                "Please enter a valid Identitiy Number",
            )
            return
        if password != confirm:
            QMessageBox.warning(self, "Error", "Passwords do not match")
            return

        success = register_user(username, email, password, name, last_name, national_id)

        if success:
            QMessageBox.information(self, "Success", "User registered successfully")
            self.open_login()
        else:
            QMessageBox.warning(self, "Error", "Username or email already exists")

    def open_login(self):
        from pages.login_page import LoginWindow

        self.login = LoginWindow()
        self.login.show()
        self.close()
