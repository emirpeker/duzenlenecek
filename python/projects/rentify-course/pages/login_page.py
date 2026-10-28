from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt6 import uic
from pathlib import Path
import sys
from services.user_service import get_user_by_identifier
import pages.car_page as car_page
from pages.main_window import MainWindow
from services.auth_service import register_user, authenticate_user
from models import user
from main import BASE_DIR


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(BASE_DIR / "ui/login.ui", self)

        try:
            self.btn_login.clicked.disconnect()
        except TypeError:
            pass

        self.btn_login.clicked.connect(self.handle_login)

        try:
            self.label_5.linkActivated.connect(self.open_signup)
        except AttributeError:
            pass

        try:
            self.pushButton.clicked.connect(self.open_signup)
        except AttributeError:
            pass

    def open_signup(self):
        from pages.signup_page import SignupWindow

        self.signup = SignupWindow()
        self.signup.show()
        self.close()

    def handle_login(self):

        username = self.le_username.text()
        password = self.le_password.text()
        if not username or not password:
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        success = authenticate_user(username, password)
        if success:
            user_obj = get_user_by_identifier(username)
            if user_obj:
                self.open_window(user_obj)
            else:
                QMessageBox.critical(
                    self, "Error", "User found but details could not be loaded!"
                )
        else:
            QMessageBox.warning(self, "Error", "Wrong username or password!")

    def open_window(self, user_obj):
        self.main_window = MainWindow(current_user=user_obj)

        try:
            self.main_window.logout_signal.connect(self.show_login_again)
        except AttributeError:
            pass

        self.main_window.showMaximized()

        self.close()

    def show_login_again(self):
        self.show()
        self.le_password.clear()
