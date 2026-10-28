# pages/main_window.py

from __future__ import annotations
from datetime import datetime
from typing import List

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QPushButton,
    QLabel,
    QStackedWidget,
    QSizePolicy,
    QSpacerItem,
    QMessageBox,
    QApplication,
)

import pages.profile_page as profile_page
import pages.car_page as car_page
import pages.dashboard_page as dashboard_page
import pages.rental_page as rental_page
import pages.reports_page as reports_page
import pages.user_reports_page as user_reports_page  # User rapor dosyası
import pages.return_page as return_page
from ui.stylesheet import APP_STYLE


class MainWindow(QMainWindow):
    logout_signal = pyqtSignal()

    def __init__(self, current_user=None):
        super().__init__()
        self.current_user = current_user
        self.setWindowTitle("Rentify")

        root = QWidget(self)
        self.setCentralWidget(root)
        main_layout = QHBoxLayout(root)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        self.nav_buttons: List[QPushButton] = []
        self.recent_events = []
        self.sidebar = self._build_sidebar()

        # Pages Stack
        self.stack = QStackedWidget()

        # 1. Dashboard
        self.page_dashboard = dashboard_page.DashboardPage(self.current_user)
        self.page_dashboard.request_rental_page.connect(self.open_rentals_page)
        self.page_dashboard.request_returns_page.connect(self.open_returns_page)

        # 2. Cars & Rentals & Returns
        self.page_cars = car_page.CarsPage(on_event=self.add_event)
        self.page_rentals = rental_page.RentalPage(self.current_user)
        self.page_returns = return_page.ReturnsPage(
            self.current_user, on_return_success=self.handle_return_refresh
        )

        # 3. Reports (KRİTİK DÜZELTME BURADA)
        if current_user.role == "admin":
            # Admin ise reports_page içindeki ReportsPage sınıfını kullan
            self.page_reports = reports_page.ReportsPage()
        else:
            # User ise user_reports_page içindeki UserReportsPage sınıfını kullan
            self.page_reports = user_reports_page.UserReportsPage(current_user)

        # 4. Profile
        self.page_profile = profile_page.ProfilePage(self.current_user)
        self.page_profile.logout_requested.connect(self.handle_logout)

        # Stack Ekleme Sırası (0-5)
        self.stack.addWidget(self.page_dashboard)  # 0
        self.stack.addWidget(self.page_cars)  # 1
        self.stack.addWidget(self.page_rentals)  # 2
        self.stack.addWidget(self.page_returns)  # 3
        self.stack.addWidget(self.page_reports)  # 4
        self.stack.addWidget(self.page_profile)  # 5

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stack)

        self.stack.currentChanged.connect(self.update_active_button_style)
        self.setStyleSheet(APP_STYLE)

        self.stack.setCurrentIndex(0)
        self.update_active_button_style(0)
        self.apply_role_permissions()
        self.refresh_dashboard()

    def _build_sidebar(self) -> QFrame:
        side = QFrame()
        side.setFixedWidth(240)
        side.setObjectName("sidebar")
        lay = QVBoxLayout(side)
        lay.setContentsMargins(14, 14, 14, 14)
        lay.setSpacing(10)

        title = QLabel("RENTIFY")
        title.setObjectName("sideTitle")

        self.btn_dashboard = self._side_btn("Homepage")
        self.btn_cars = self._side_btn("Cars")
        self.btn_rentals = self._side_btn("Rentals")
        self.btn_returns = self._side_btn("Returns")
        self.btn_reports = self._side_btn("Reports")
        self.btn_profile = self._side_btn("Profile")
        self.btn_exit = self._side_btn("Exit")

        lay.addWidget(title)
        lay.addSpacing(8)
        lay.addWidget(self.btn_dashboard)
        lay.addWidget(self.btn_cars)
        lay.addWidget(self.btn_rentals)
        lay.addWidget(self.btn_returns)
        lay.addWidget(self.btn_reports)
        lay.addWidget(self.btn_profile)

        # Exit butonu en alta
        lay.addStretch(1)
        lay.addWidget(self.btn_exit)

        # Sinyaller
        self.btn_dashboard.clicked.connect(
            lambda: (self.refresh_dashboard(), self.stack.setCurrentIndex(0))
        )
        self.btn_cars.clicked.connect(self.open_cars_page)
        self.btn_rentals.clicked.connect(self.open_rentals_page)
        self.btn_returns.clicked.connect(self.open_returns_page)
        self.btn_reports.clicked.connect(self.open_reports_page)
        self.btn_profile.clicked.connect(lambda: self.stack.setCurrentIndex(5))
        self.btn_exit.clicked.connect(self.handle_exit)

        return side

    def _side_btn(self, text):
        b = QPushButton(text)
        b.setCursor(Qt.CursorShape.PointingHandCursor)
        b.setFixedHeight(40)
        b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        b.setObjectName("sideBtn")
        if text != "Exit":
            self.nav_buttons.append(b)
        return b

    # --- Navigation Helpers ---
    def open_cars_page(self):
        self.refresh_cars_page()
        self.stack.setCurrentIndex(1)

    def open_rentals_page(self, plate=None):
        if hasattr(self.page_rentals, "load_data"):
            self.page_rentals.load_data()
        self.stack.setCurrentIndex(2)
        if plate and hasattr(self.page_rentals, "select_car_by_plate"):
            self.page_rentals.select_car_by_plate(plate)

    def open_returns_page(self):
        self.page_returns.load_rentals()
        self.stack.setCurrentIndex(3)

    def open_reports_page(self):
        if hasattr(self.page_reports, "load_data"):
            self.page_reports.load_data()
        self.stack.setCurrentIndex(4)

    def refresh_cars_page(self):
        if hasattr(self.page_cars, "reload_cars_from_db"):
            self.page_cars.reload_cars_from_db()
        elif hasattr(self.page_cars, "refresh_table"):
            self.page_cars.refresh_table()

    def update_active_button_style(self, index):
        for i, btn in enumerate(self.nav_buttons):
            btn.setProperty("active", i == index)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    def add_event(self, action, plate, user="admin"):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.recent_events.insert(0, (ts, action, plate, user))
        self.recent_events = self.recent_events[:20]
        self.refresh_dashboard()

    def refresh_dashboard(self):
        if hasattr(self, "page_dashboard"):
            self.page_dashboard.load_data()

    def handle_exit(self):
        if (
            QMessageBox.question(
                self,
                "Exit",
                "Quit application?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            == QMessageBox.StandardButton.Yes
        ):
            QApplication.instance().quit()

    def handle_logout(self):
        if (
            QMessageBox.question(
                self,
                "Logout",
                "Log out?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            == QMessageBox.StandardButton.Yes
        ):
            self.close()
            self.logout_signal.emit()

    def apply_role_permissions(self):
        if not self.current_user:
            return
        if self.current_user.role == "user":
            if hasattr(self, "btn_cars"):
                self.btn_cars.hide()

    def handle_return_refresh(self):
        self.refresh_cars_page()
        if hasattr(self, "page_rentals"):
            self.page_rentals.load_data()
        if hasattr(self, "page_reports"):
            self.page_reports.load_data()
        self.refresh_dashboard()
