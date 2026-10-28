# pages/rental_page.py

from __future__ import annotations
from datetime import date

from PyQt6.QtCore import Qt, QDate, QLocale, QSize
from PyQt6.QtGui import QIcon, QAction, QColor
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QDateEdit,
    QComboBox,
    QFrame,
    QFormLayout,
    QAbstractItemView,
    QStackedLayout,
    QGridLayout,
    QSizePolicy,
)

from models.car import Car
from services.car_service import get_available_cars
from services.rental_service import rent_car, get_user_discount_rate


class RentalPage(QWidget):
    def __init__(self, current_user):
        super().__init__()
        self.setObjectName("RentalPageWidget")
        self.current_user = current_user
        self._cars = []
        self._filtered_cars = []
        self.selected_car = None

        self.init_ui()
        self.load_data()

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(30)

        # =================================================
        # SOL PANEL: ARAÇ LİSTESİ
        # =================================================
        left_panel = QVBoxLayout()
        left_panel.setSpacing(20)

        # 1. Başlık
        title = QLabel("Find Your Perfect Drive")
        title.setObjectName("pageTitle")  # Stylesheet'ten stili çeker
        left_panel.addWidget(title)

        # 2. Filtre ve Arama
        filter_frame = QFrame()
        filter_frame.setObjectName("filterFrame")  # Stylesheet'ten
        filter_layout = QHBoxLayout(filter_frame)
        filter_layout.setContentsMargins(10, 10, 10, 10)

        self.cb_brand_filter = QComboBox()
        self.cb_brand_filter.addItem("All Brands")
        self.cb_brand_filter.setFixedWidth(150)
        self.cb_brand_filter.setFixedHeight(40)
        # Inline stil silindi -> Stylesheet'teki QComboBox stili geçerli
        self.cb_brand_filter.currentTextChanged.connect(self.apply_filters)

        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText("Search by model...")
        self.le_search.setFixedHeight(40)
        # Inline stil silindi -> Stylesheet'teki QLineEdit stili geçerli

        search_action = QAction(QIcon("ui/icons/search.png"), "", self.le_search)
        self.le_search.addAction(
            search_action, QLineEdit.ActionPosition.TrailingPosition
        )
        self.le_search.textChanged.connect(self.apply_filters)

        filter_layout.addWidget(self.cb_brand_filter)
        filter_layout.addWidget(self.le_search)
        left_panel.addWidget(filter_frame)

        # 3. Tablo
        self.content_stack = QStackedLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Brand", "Model", "Plate", "Daily Price", "Current KM"]
        )
        # Inline stil silindi -> Stylesheet'teki QTableWidget stili geçerli
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # Sütun Genişlikleri
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.table.setColumnWidth(3, 130)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.on_row_selected)

        # Boş Durum
        self.empty_widget = QWidget()
        empty_layout = QVBoxLayout(self.empty_widget)
        lbl_empty_icon = QLabel("🔍")
        lbl_empty_icon.setStyleSheet("font-size: 50px; border:none;")
        lbl_empty_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_empty_text = QLabel("No cars found.")
        lbl_empty_text.setObjectName("labelGray")
        lbl_empty_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_layout.addStretch()
        empty_layout.addWidget(lbl_empty_icon)
        empty_layout.addWidget(lbl_empty_text)
        empty_layout.addStretch()

        self.content_stack.addWidget(self.table)
        self.content_stack.addWidget(self.empty_widget)

        left_panel.addLayout(self.content_stack)
        main_layout.addLayout(left_panel, 65)

        # =================================================
        # SAĞ PANEL: BOOKING SUMMARY
        # =================================================
        right_panel = QVBoxLayout()
        right_panel.setContentsMargins(0, 60, 0, 0)

        self.summary_card = QFrame()
        self.summary_card.setObjectName(
            "summaryCard"
        )  # Stylesheet'ten özel stil alacak

        card_layout = QVBoxLayout(self.summary_card)
        card_layout.setContentsMargins(25, 30, 25, 30)
        card_layout.setSpacing(20)

        # Başlık
        lbl_sum_title = QLabel("Booking Summary")
        lbl_sum_title.setObjectName("sectionTitle")
        card_layout.addWidget(lbl_sum_title)

        # Seçili Araç
        self.car_header_layout = QHBoxLayout()

        self.lbl_car_img = QLabel("🚘")
        self.lbl_car_img.setFixedSize(50, 50)
        self.lbl_car_img.setStyleSheet(
            "background-color: #f1f5f9; border-radius: 12px; font-size: 24px; qproperty-alignment: AlignCenter;"
        )

        car_text_layout = QVBoxLayout()
        car_text_layout.setSpacing(2)
        self.lbl_car_model = QLabel("Select a car")
        self.lbl_car_model.setObjectName("sectionTitle")
        self.lbl_car_model.setStyleSheet("font-size: 16px;")  # Local override gerekirse
        self.lbl_car_plate = QLabel("to see details")
        self.lbl_car_plate.setObjectName("labelGray")

        car_text_layout.addWidget(self.lbl_car_model)
        car_text_layout.addWidget(self.lbl_car_plate)

        self.car_header_layout.addWidget(self.lbl_car_img)
        self.car_header_layout.addLayout(car_text_layout)
        self.car_header_layout.addStretch()

        card_layout.addLayout(self.car_header_layout)

        # Ayırıcı
        line1 = QFrame()
        line1.setFrameShape(QFrame.Shape.HLine)
        line1.setStyleSheet("color: #f1f5f9;")
        card_layout.addWidget(line1)

        # Tarih Seçimi
        date_layout = QGridLayout()
        date_layout.setVerticalSpacing(15)
        date_layout.setHorizontalSpacing(15)

        lbl_pickup = QLabel("Pick-up:")
        lbl_pickup.setObjectName("labelGray")
        self.date_start = QDateEdit()
        self.date_start.setCalendarPopup(True)
        self.date_start.setDate(QDate.currentDate())
        self.date_start.setMinimumDate(QDate.currentDate())
        self.date_start.setFixedHeight(40)
        # _get_date_style kaldırıldı, stylesheet'ten alacak
        self.date_start.dateChanged.connect(self.calculate_total)

        lbl_dropoff = QLabel("Drop-off:")
        lbl_dropoff.setObjectName("labelGray")
        self.date_end = QDateEdit()
        self.date_end.setCalendarPopup(True)
        self.date_end.setDate(QDate.currentDate().addDays(1))
        self.date_end.setMinimumDate(QDate.currentDate().addDays(1))
        self.date_end.setFixedHeight(40)
        self.date_end.dateChanged.connect(self.calculate_total)

        date_layout.addWidget(lbl_pickup, 0, 0)
        date_layout.addWidget(self.date_start, 0, 1)
        date_layout.addWidget(lbl_dropoff, 1, 0)
        date_layout.addWidget(self.date_end, 1, 1)

        card_layout.addLayout(date_layout)

        card_layout.addSpacing(10)

        # Fiyat Dökümü
        self.grid_breakdown = QGridLayout()
        self.grid_breakdown.setVerticalSpacing(10)

        self.grid_breakdown.addWidget(QLabel("Daily Rate:"), 0, 0)
        self.val_daily = QLabel("0 TL")
        self.val_daily.setObjectName("labelDark")
        self.val_daily.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.grid_breakdown.addWidget(self.val_daily, 0, 1)

        self.grid_breakdown.addWidget(QLabel("Duration:"), 1, 0)
        self.val_duration = QLabel("0 Days")
        self.val_duration.setObjectName("labelDark")
        self.val_duration.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.grid_breakdown.addWidget(self.val_duration, 1, 1)

        self.grid_breakdown.addWidget(QLabel("Subtotal:"), 2, 0)
        self.val_subtotal = QLabel("0 TL")
        self.val_subtotal.setObjectName("labelDark")
        self.val_subtotal.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.grid_breakdown.addWidget(self.val_subtotal, 2, 1)

        self.lbl_disc_title = QLabel("Discount:")
        self.lbl_disc_title.setObjectName("labelSuccess")
        self.val_discount = QLabel("-0 TL")
        self.val_discount.setObjectName("labelSuccess")
        self.val_discount.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.grid_breakdown.addWidget(self.lbl_disc_title, 3, 0)
        self.grid_breakdown.addWidget(self.val_discount, 3, 1)

        # Sol etiketlere stil ata
        for i in range(3):
            item = self.grid_breakdown.itemAtPosition(i, 0).widget()
            item.setObjectName("labelGray")

        card_layout.addLayout(self.grid_breakdown)

        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setStyleSheet("color: #f1f5f9;")
        card_layout.addWidget(line2)

        # Toplam Tutar
        total_layout = QHBoxLayout()
        lbl_total_txt = QLabel("TOTAL PAY:")
        lbl_total_txt.setObjectName("labelGray")
        lbl_total_txt.setStyleSheet("font-weight: bold;")

        self.val_total = QLabel("0 TL")
        self.val_total.setObjectName("labelTotal")

        total_layout.addWidget(lbl_total_txt)
        total_layout.addStretch()
        total_layout.addWidget(self.val_total)

        card_layout.addLayout(total_layout)
        card_layout.addStretch()

        # Buton
        lbl_legal = QLabel("By confirming, you agree to the rental terms.")
        lbl_legal.setObjectName("labelGray")
        lbl_legal.setStyleSheet("font-size: 11px; margin-bottom: 5px;")
        lbl_legal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(lbl_legal)

        self.btn_confirm = QPushButton("Confirm Rental")
        self.btn_confirm.setObjectName(
            "primaryBtn"
        )  # Stylesheet'ten Primary Button stili
        self.btn_confirm.setFixedHeight(55)
        self.btn_confirm.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_confirm.clicked.connect(self.handle_rent)
        self.btn_confirm.setEnabled(False)

        card_layout.addWidget(self.btn_confirm)

        right_panel.addWidget(self.summary_card)
        main_layout.addLayout(right_panel, 35)

    def load_data(self):
        self._cars = get_available_cars()
        self._filtered_cars = self._cars.copy()
        self.populate_brands()
        self.refresh_table()

    def populate_brands(self):
        self.cb_brand_filter.blockSignals(True)
        brands = sorted(list(set(c.brand for c in self._cars)))
        self.cb_brand_filter.clear()
        self.cb_brand_filter.addItem("All Brands")
        self.cb_brand_filter.addItems(brands)
        self.cb_brand_filter.blockSignals(False)

    def apply_filters(self):
        brand = self.cb_brand_filter.currentText()
        search = self.le_search.text().lower()

        self._filtered_cars = []
        for c in self._cars:
            if "All Brands" not in brand and c.brand != brand:
                continue
            if search and (
                search not in c.model.lower() and search not in c.plate_number.lower()
            ):
                continue
            self._filtered_cars.append(c)

        self.refresh_table()

    def refresh_table(self):
        self.table.setSortingEnabled(False)  #  ekle
        self.table.setRowCount(0)

        if not self._filtered_cars:
            self.content_stack.setCurrentIndex(1)
            return

        self.content_stack.setCurrentIndex(0)

        for car in self._filtered_cars:
            row = self.table.rowCount()
            self.table.insertRow(row)

            item_brand = QTableWidgetItem(car.brand)
            f = item_brand.font()
            f.setBold(True)
            item_brand.setFont(f)

            # car objesini UserRole’a koyuyorsun (iyi)
            item_brand.setData(Qt.ItemDataRole.UserRole, car)
            self.table.setItem(row, 0, item_brand)

            self.table.setItem(row, 1, QTableWidgetItem(car.model))
            self.table.setItem(row, 2, QTableWidgetItem(car.plate_number))
            self.table.setItem(row, 3, QTableWidgetItem(f"{int(car.daily_price)} TL"))

            item_km = QTableWidgetItem(f"{car.kilometer} km")
            item_km.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 4, item_km)
        self.clear_selection()

    def clear_selection(self):
        self.selected_car = None
        self.lbl_car_model.setText("Select a car")
        self.lbl_car_plate.setText("to see details")
        self.lbl_car_img.setText("🚗")

        self.val_daily.setText("-")
        self.val_duration.setText("-")
        self.val_subtotal.setText("-")
        self.val_discount.setText("-")
        self.val_total.setText("0 TL")

        self.lbl_disc_title.setVisible(False)
        self.val_discount.setVisible(False)
        self.btn_confirm.setEnabled(False)

    def on_row_selected(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return

        item = self.table.item(current_row, 0)
        if not item:
            return

        car = item.data(Qt.ItemDataRole.UserRole)
        self.selected_car = car

        self.lbl_car_model.setText(f"{car.brand} {car.model}")
        self.lbl_car_plate.setText(f"Plate: {car.plate_number}")

        self.btn_confirm.setEnabled(True)
        self.calculate_total()

    def calculate_total(self):
        if not getattr(self, "selected_car", None):
            return

        start = self.date_start.date().toPyDate()
        end = self.date_end.date().toPyDate()

        if end <= start:
            self.val_total.setText("Invalid Date")
            self.btn_confirm.setEnabled(False)
            return

        self.btn_confirm.setEnabled(True)
        days = (end - start).days
        daily_price = float(self.selected_car.daily_price)

        rate, tier = get_user_discount_rate(self.current_user.id)
        base_total = days * daily_price
        discount_amount = base_total * rate
        final_total = base_total - discount_amount

        self.val_daily.setText(f"{int(daily_price)} TL")
        self.val_duration.setText(f"{days} Days")
        self.val_subtotal.setText(f"{int(base_total)} TL")

        if rate > 0:
            self.lbl_disc_title.setVisible(True)
            self.val_discount.setVisible(True)
            self.val_discount.setText(f"-{int(discount_amount)} TL ({tier})")
        else:
            self.lbl_disc_title.setVisible(False)
            self.val_discount.setVisible(False)

        self.val_total.setText(f"{int(final_total)} TL")

    def handle_rent(self):
        if not getattr(self, "selected_car", None):
            return

        total_msg = self.val_total.text()
        msg = f"Rent {self.selected_car.brand} {self.selected_car.model}?\n\nTotal Payment: {total_msg}"
        reply = QMessageBox.question(
            self,
            "Confirm Rental",
            msg,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            start = self.date_start.date().toPyDate()
            days = (self.date_end.date().toPyDate() - start).days

            success, message = rent_car(
                self.selected_car.id, self.current_user.id, days, start_date=str(start)
            )

            if success:
                QMessageBox.information(self, "Success", message)
                self.clear_selection()
                self.load_data()
            else:
                QMessageBox.critical(self, "Error", message)

    def select_car_by_plate(self, plate_number):
        self.cb_brand_filter.setCurrentIndex(0)
        self.le_search.clear()
        self.apply_filters()

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 2)
            if item and item.text() == plate_number:
                self.table.selectRow(row)
                self.on_row_selected()
                self.table.scrollToItem(item)
                break
