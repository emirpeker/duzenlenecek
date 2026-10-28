from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QFrame,
    QMessageBox,
    QSpacerItem,
    QSizePolicy,
    QDialog,
    QHBoxLayout,
    QInputDialog,
)
from PyQt6.QtCore import Qt, pyqtSignal
from services.user_service import (
    get_user_by_identifier,
    update_user_contact_info,
    change_password,
)
from services.password_utils import check_password, hash_password
from ui.stylesheet import PASSWORD_DIALOG_STYLE


class ProfilePage(QWidget):
    logout_requested = pyqtSignal()  # MainWindow'a logout isteği göndermek için

    def __init__(self, current_user):
        super().__init__()
        self.current_user = current_user
        self.init_ui()
        self.load_data()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        title = QLabel("User Profile")
        title.setObjectName("pageTitle")
        title.setStyleSheet("font-size:24px; font-weight:bold; color:#2c3e50;")
        layout.addWidget(title)

        card = QFrame()
        card.setObjectName("contentFrame")
        card.setStyleSheet(
            """
            QFrame#contentFrame {
                background-color: #ffffff;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: #f9f9f9;
                color: #0F172A;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
                background-color: #ffffff;
            }
        """
        )

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setSpacing(20)

        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        self.txt_username = QLineEdit()
        self.txt_username.setReadOnly(True)  # kullanıcı adı değiştrilemez
        self.txt_username.setStyleSheet("color: gray; background-color: #eaeaea;")

        self.txt_name = QLineEdit()
        self.txt_name.setReadOnly(True)  # isim değiştrilemez
        self.txt_name.setStyleSheet("color: gray; background-color: #eaeaea;")

        self.txt_lastname = QLineEdit()
        self.txt_lastname.setReadOnly(True)  # soyisim değiştrilemez
        self.txt_lastname.setStyleSheet("color: gray; background-color: #eaeaea;")

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("Your E-Mail address...")

        self.btn_change_pass = QPushButton("Change Password")
        self.btn_change_pass.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_change_pass.setStyleSheet(
            """
            QPushButton {
                background-color: #5865F2; 
                color: white; 
                border-radius: 4px; 
                padding: 8px; 
                font-weight: bold;
                text-align: center;
            }
            QPushButton:hover { background-color: #4752c4; }
        """
        )
        self.btn_change_pass.clicked.connect(self.open_password_dialog)

        self.txt_role = QLineEdit()
        self.txt_role.setReadOnly(True)  # rol değiştirilemez
        self.txt_role.setStyleSheet("color: gray; background-color: #eaeaea;")

        form_layout.addRow(QLabel("<b>Username:</b>"), self.txt_username)
        form_layout.addRow(QLabel("<b>Name:</b>"), self.txt_name)
        form_layout.addRow(QLabel("<b>Lastname:</b>"), self.txt_lastname)
        form_layout.addRow(QLabel("<b>E-Mail:</b>"), self.txt_email)
        form_layout.addRow(QLabel("<b>Password:</b>"), self.btn_change_pass)
        form_layout.addRow(QLabel("<b>Authority:</b>"), self.txt_role)

        card_layout.addLayout(form_layout)
        # BUTONLAR
        btn_layout = QHBoxLayout()

        self.btn_logout = QPushButton("Logout")
        self.btn_logout.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_logout.setFixedSize(120, 40)
        self.btn_logout.setStyleSheet(
            """
            QPushButton {
                background-color: #ef4444;
                color: white;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #dc2626; }
        """
        )
        self.btn_logout.clicked.connect(self._request_logout)

        self.btn_save = QPushButton("Save Changes")
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_save.setFixedSize(180, 40)
        self.btn_save.setStyleSheet(
            """
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #2ecc71; }
        """
        )
        self.btn_save.clicked.connect(self.save_changes)

        btn_layout.addWidget(self.btn_logout)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_save)

        card_layout.addLayout(btn_layout)

        layout.addWidget(card)
        layout.addItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

    def load_data(self):
        user_obj = self.current_user
        if not user_obj:
            QMessageBox.warning(self, "Error", "Failed to load user details!")
            return

        self.current_user = user_obj
        self.txt_username.setText(user_obj.username)
        self.txt_name.setText(str(user_obj.name).title())
        self.txt_lastname.setText(str(user_obj.lastname).title())
        self.txt_email.setText(user_obj.email)
        self.txt_role.setText(user_obj.role)

    def save_changes(self):
        new_email = self.txt_email.text().strip()
        if not new_email:
            QMessageBox.warning(self, "Error", "Email address is required.")
            return

        if new_email == self.current_user.email:
            QMessageBox.information(self, "Info", "No changes made.")
            return

        success = update_user_contact_info(self.current_user.username, new_email, None)
        if success:
            QMessageBox.information(self, "Success", "Profile updated successfully.")
            if self.current_user:
                self.current_user.email = new_email
            else:
                QMessageBox.critical(self, "Error", "Database update failed.")

    def _request_logout(self):
        self.logout_requested.emit()  # MainWindow'a logout isteği göndermek için

    def open_password_dialog(self):
        dialog = PasswordChangeDialog(self.current_user, parent=self)
        dialog.exec()


class PasswordChangeDialog(QDialog):
    def __init__(self, current_user, parent=None):
        super().__init__(parent)
        self.current_user = current_user

        self.setWindowTitle("Update Password")
        self.setFixedSize(440, 420)
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint
        )
        self.setStyleSheet(PASSWORD_DIALOG_STYLE)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Update Password")
        title.setObjectName("dialogTitle")
        layout.addWidget(title)

        desc = QLabel("Enter your current password and a new password.")
        desc.setObjectName("dialogDesc")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        layout.addWidget(QLabel("CURRENT PASSWORD *"))
        self.input_old = QLineEdit()
        self.input_old.setEchoMode(QLineEdit.EchoMode.Password)  # Şifreyi gizler
        layout.addWidget(self.input_old)

        layout.addWidget(QLabel("NEW PASSWORD *"))
        self.input_new = QLineEdit()
        self.input_new.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_new)

        layout.addWidget(QLabel("CONFIRM NEW PASSWORD *"))
        self.input_confirm = QLineEdit()
        self.input_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_confirm)

        layout.addStretch()

        btn_layout = QHBoxLayout()

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setObjectName("cancelBtn")
        self.btn_cancel.clicked.connect(self.reject)

        self.btn_save = QPushButton("Done")
        self.btn_save.setObjectName("saveBtn")
        self.btn_save.clicked.connect(self.handle_save)

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_save)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.btn_save = QPushButton("Done")
        self.btn_save.setObjectName("saveBtn")
        self.btn_save.setDefault(True)
        self.btn_save.setAutoDefault(True)  # Enter ile işlem yapabilmek için
        self.btn_save.clicked.connect(self.handle_save)

    def handle_save(self):
        try:
            old_pass = self.input_old.text().strip()
            new_pass = self.input_new.text().strip()
            confirm_pass = self.input_confirm.text().strip()  # kullanıcı girişleri

            if not old_pass or not new_pass or not confirm_pass:
                QMessageBox.warning(self, "Error", "Please fill in all fields.")
                return

            if len(new_pass) < 8:  # validation
                QMessageBox.warning(
                    self, "Error", "New password must be at least 8 characters long."
                )
                return

            if old_pass == new_pass:
                QMessageBox.warning(
                    self,
                    "Error",
                    "New password cannot be the same as the current password.",
                )
                return

            if new_pass != confirm_pass:
                QMessageBox.warning(self, "Error", "New passwords do not match!")
                return

            is_success, msg = change_password(
                self.current_user.username, old_pass, new_pass
            )  # servis çağrısı

            if is_success:
                QMessageBox.information(self, "Success", msg)
                self.current_user.password = hash_password(new_pass)  # hash i güncelle
                self.accept()
            else:
                QMessageBox.critical(self, "Error", msg)

        except Exception:
            QMessageBox.critical(self, "Error", "Unexpected system error occurred.")

    def keyPressEvent(self, event):
        if event.key() in (
            Qt.Key.Key_Return,
            Qt.Key.Key_Enter,
        ):  # Enter, Done butonuna basılmış gibi davranır
            self.handle_save()
            return
        super().keyPressEvent(event)
