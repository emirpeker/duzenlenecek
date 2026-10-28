from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt6 import uic
from pathlib import Path
import sys
import pages.car_page as car_page
from pages.main_window import MainWindow
from ui.stylesheet import APP_STYLE

BASE_DIR = Path(__file__).resolve().parent
if __name__ == "__main__":
    from pages.login_page import LoginWindow

    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
