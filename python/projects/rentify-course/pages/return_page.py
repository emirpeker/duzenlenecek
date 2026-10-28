# pages/returns_page.py

from __future__ import annotations
from datetime import date

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QFrame,
    QTextEdit,
    QSpinBox,
    QGridLayout,
    QDateEdit,
    QComboBox,
    QAbstractItemView,
    QStackedLayout,
    QSizePolicy,
)
from PyQt6.QtCore import QDate, Qt, QLocale
from PyQt6.QtGui import QIcon, QAction, QColor, QBrush

from services.rental_service import get_active_rentals
from services.return_service import calculate_late_fee, process_detailed_return


class ReturnsPage(QWidget):
    def __init__(self, current_user, on_return_success=None):
        super().__init__()
        self.setObjectName("ReturnsPageWidget")

        self.current_user = current_user
        self.on_return_success = on_return_success

        self.active_rentals = []
        self.filtered_rentals = []
        self.selected_rental = None

        self.init_ui()
        self.load_rentals()

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(30)

        # =================================================
        # SOL PANEL
        # =================================================
        left_panel = QVBoxLayout()
        left_panel.setSpacing(20)

        title_layout = QHBoxLayout()
        title = QLabel("Active Rentals")
        title.setObjectName("pageTitle")

        self.lbl_stats = QLabel("Loading...")
        self.lbl_stats.setStyleSheet("color:#64748b; font-size:13px; font-weight:600;")

        title_layout.addWidget(title)
        title_layout.addWidget(self.lbl_stats)
        title_layout.addStretch()
        left_panel.addLayout(title_layout)

        # Filtreler
        filter_frame = QFrame()
        filter_frame.setObjectName("filterFrame")
        filter_layout = QHBoxLayout(filter_frame)
        filter_layout.setContentsMargins(10, 10, 10, 10)

        self.cb_brand_filter = QComboBox()
        self.cb_brand_filter.addItem("All Brands")
        self.cb_brand_filter.setFixedWidth(140)
        self.cb_brand_filter.setFixedHeight(40)
        self.cb_brand_filter.currentTextChanged.connect(self.filter_data)

        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText("Search Plate, Model or Customer...")
        self.le_search.setFixedHeight(40)

        search_action = QAction(QIcon("ui/icons/search.png"), "", self.le_search)
        self.le_search.addAction(
            search_action, QLineEdit.ActionPosition.TrailingPosition
        )
        self.le_search.textChanged.connect(self.filter_data)

        filter_layout.addWidget(self.cb_brand_filter)
        filter_layout.addWidget(self.le_search)
        left_panel.addWidget(filter_frame)

        # =================================================
        #  TABLO
        # =================================================
        self.content_stack = QStackedLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Plate", "Brand / Model", "Customer", "Expected Return", "Status"]
        )

        #
        self.table.setSortingEnabled(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.on_row_selected)

        # Boş Durum
        self.empty_widget = QWidget()
        empty_layout = QVBoxLayout(self.empty_widget)
        lbl_empty_icon = QLabel("📂")
        lbl_empty_icon.setStyleSheet("font-size:50px; border:none;")
        lbl_empty_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_empty_text = QLabel("No active rentals found.")
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
        # SAĞ PANEL: RENTAL PAGE TARZI MODERN YAPI
        # =================================================
        right_panel = QVBoxLayout()
        right_panel.setContentsMargins(0, 60, 0, 0)

        self.card_frame = QFrame()
        self.card_frame.setObjectName("summaryCard")

        card_layout = QVBoxLayout(self.card_frame)
        card_layout.setContentsMargins(25, 30, 25, 30)
        card_layout.setSpacing(20)

        # 2. Araç Bilgi Alanı (RentalPage ile aynı yapı)
        self.car_header_layout = QHBoxLayout()

        # İkon
        self.lbl_car_img = QLabel("🚗")
        self.lbl_car_img.setFixedSize(50, 50)
        self.lbl_car_img.setStyleSheet(
            "background-color: #f1f5f9; border-radius: 12px; font-size: 24px; qproperty-alignment: AlignCenter;"
        )

        # Yazılar
        car_text_layout = QVBoxLayout()
        car_text_layout.setSpacing(2)

        self.lbl_car_model = QLabel("Select a rental")
        self.lbl_car_model.setStyleSheet(
            "font-size: 16px; font-weight: bold; color: #334155;"
        )

        self.lbl_car_plate = QLabel("to see details")
        self.lbl_car_plate.setStyleSheet("font-size: 13px; color: #64748b;")

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

        # 3. Form Alanı (Grid)
        self.form_container = QWidget()
        # Başlangıçta formu devre dışı bırak
        self.form_container.setEnabled(False)

        form_layout = QGridLayout(self.form_container)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setVerticalSpacing(15)
        form_layout.setHorizontalSpacing(15)

        self.date_return = QDateEdit()
        self.date_return.setCalendarPopup(True)
        self.date_return.setDisplayFormat("dd.MM.yyyy")
        self.date_return.setDate(QDate.currentDate())
        self.date_return.setFixedHeight(40)
        self.date_return.dateChanged.connect(self.calculate_total)
        self.date_return.setLocale(QLocale(QLocale.Language.English))

        self.inp_km = QSpinBox()
        self.inp_km.setRange(0, 9999999)
        self.inp_km.setSuffix(" km")
        self.inp_km.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.inp_km.setFixedHeight(40)
        self.inp_km.valueChanged.connect(self.validate_km)

        self.inp_damage = QLineEdit()
        self.inp_damage.setPlaceholderText("0")
        self.inp_damage.setFixedHeight(40)
        self.inp_damage.textChanged.connect(self.calculate_total)

        self.inp_notes = QTextEdit()
        self.inp_notes.setPlaceholderText("Condition notes...")
        self.inp_notes.setMaximumHeight(60)
        self.inp_notes.setStyleSheet(
            """
            QTextEdit {
                border: 1px solid #e2e8f0; border-radius: 10px; padding: 10px;
                background-color: white; color: #334155; font-weight: bold;
            }
            QTextEdit:focus { border: 2px solid #3b82f6; }
        """
        )

        # Etiketler
        l_date = QLabel("Return Date:")
        l_date.setObjectName("labelGray")
        l_km = QLabel("End KM:")
        l_km.setObjectName("labelGray")
        l_dmg = QLabel("Damage Fee:")
        l_dmg.setObjectName("labelGray")
        l_note = QLabel("Notes:")
        l_note.setObjectName("labelGray")

        form_layout.addWidget(l_date, 0, 0)
        form_layout.addWidget(self.date_return, 0, 1)

        form_layout.addWidget(l_km, 1, 0)
        form_layout.addWidget(self.inp_km, 1, 1)

        form_layout.addWidget(l_dmg, 2, 0)
        form_layout.addWidget(self.inp_damage, 2, 1)

        # Notes Hizalaması Düzeltildi (AlignTop)
        form_layout.addWidget(l_note, 3, 0, Qt.AlignmentFlag.AlignTop)
        form_layout.addWidget(self.inp_notes, 3, 1)

        card_layout.addWidget(self.form_container)
        card_layout.addSpacing(10)

        # 4. Fiyat Dökümü
        self.breakdown_widget = QWidget()
        bd_layout = QGridLayout(self.breakdown_widget)
        bd_layout.setContentsMargins(0, 0, 0, 0)
        bd_layout.setVerticalSpacing(8)

        self.lbl_bd_base = QLabel("0 TL")
        self.lbl_bd_base.setObjectName("labelDark")
        self.lbl_bd_base.setAlignment(Qt.AlignmentFlag.AlignRight)
        bd_layout.addWidget(QLabel("Base Price:"), 0, 0)
        bd_layout.addWidget(self.lbl_bd_base, 0, 1)

        self.lbl_bd_late = QLabel("0 TL")
        self.lbl_bd_late.setObjectName("labelDanger")
        self.lbl_bd_late.setAlignment(Qt.AlignmentFlag.AlignRight)
        bd_layout.addWidget(QLabel("Late Fee:"), 1, 0)
        bd_layout.addWidget(self.lbl_bd_late, 1, 1)

        self.lbl_bd_damage = QLabel("0 TL")
        self.lbl_bd_damage.setObjectName("labelDark")
        self.lbl_bd_damage.setAlignment(Qt.AlignmentFlag.AlignRight)
        bd_layout.addWidget(QLabel("Damage Fee:"), 2, 0)
        bd_layout.addWidget(self.lbl_bd_damage, 2, 1)

        # Sol etiketlere stil
        for i in range(3):
            item = bd_layout.itemAtPosition(i, 0).widget()
            if item:
                item.setObjectName("labelGray")

        card_layout.addWidget(self.breakdown_widget)

        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setStyleSheet("color: #f1f5f9;")
        card_layout.addWidget(line2)

        # 5. Toplam Tutar
        total_cont = QHBoxLayout()
        l_total = QLabel("TOTAL PAY:")
        l_total.setObjectName("labelGray")
        l_total.setStyleSheet("font-weight: bold;")
        self.txt_total = QLabel("0 TL")
        self.txt_total.setObjectName("labelTotal")

        total_cont.addWidget(l_total)
        total_cont.addStretch()
        total_cont.addWidget(self.txt_total)

        card_layout.addLayout(total_cont)
        card_layout.addStretch()

        # Yasal Uyarı
        lbl_disclaimer = QLabel("Once confirmed, this action cannot be undone.")
        lbl_disclaimer.setStyleSheet(
            "color: #94a3b8; font-size: 11px; margin-bottom: 5px;"
        )
        lbl_disclaimer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(lbl_disclaimer)

        # Buton
        self.btn_confirm = QPushButton("Confirm Return")
        self.btn_confirm.setObjectName("primaryBtn")
        self.btn_confirm.setFixedHeight(55)
        self.btn_confirm.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_confirm.clicked.connect(self.handle_return)
        self.btn_confirm.setEnabled(False)

        card_layout.addWidget(self.btn_confirm)

        right_panel.addWidget(self.card_frame)
        main_layout.addLayout(right_panel, 35)

    def load_rentals(self):
        if not self.current_user:
            return
        self.active_rentals = get_active_rentals(
            self.current_user.id, self.current_user.role
        )

        if self.current_user.role != "admin":
            self.table.setColumnHidden(2, True)
        else:
            self.table.setColumnHidden(2, False)

        self.cb_brand_filter.blockSignals(True)
        self.cb_brand_filter.clear()
        self.cb_brand_filter.addItem("All Brands")
        brands = sorted(list(set(r["brand"] for r in self.active_rentals)))
        self.cb_brand_filter.addItems(brands)
        self.cb_brand_filter.blockSignals(False)

        self.update_stats()
        self.filter_data()

    def update_stats(self):
        total = len(self.active_rentals)
        today = date.today()
        late_count = sum(
            1
            for r in self.active_rentals
            if r.get("end_date") and r.get("end_date") < today
        )

        stat_text = f"{total} Active Rentals  •  {late_count} Late Returns"
        if self.current_user.role == "admin":
            daily_rev = sum(float(r["daily_price"]) for r in self.active_rentals)
            stat_text += f"  •  Daily Revenue: {int(daily_rev)} TL"

        self.lbl_stats.setText(stat_text)

    def filter_data(self):
        query = self.le_search.text().lower().strip()
        selected_brand = self.cb_brand_filter.currentText()
        self.filtered_rentals = []
        for row in self.active_rentals:
            if selected_brand != "All Brands" and row["brand"] != selected_brand:
                continue
            content = f"{row['plate_number']} {row['model']} {row['username']}".lower()
            if query and query not in content:
                continue
            self.filtered_rentals.append(row)
        self.refresh_table()

    def refresh_table(self):
        self.table.setRowCount(0)
        today = date.today()

        if not self.filtered_rentals:
            self.content_stack.setCurrentIndex(1)
            return
        self.content_stack.setCurrentIndex(0)

        for row in self.filtered_rentals:
            r_idx = self.table.rowCount()
            self.table.insertRow(r_idx)

            # 1. Plate (Normal Font)
            item_plate = QTableWidgetItem(row.get("plate_number", "-"))
            item_plate.setData(Qt.ItemDataRole.UserRole, row)
            self.table.setItem(r_idx, 0, item_plate)

            # 2. Brand / Model (Kalın ve Ortada)
            brand_model_str = f"{row.get('brand','')} {row.get('model','')}"
            item_model = QTableWidgetItem(brand_model_str)
            f_model = item_model.font()
            f_model.setBold(True)
            item_model.setFont(f_model)
            item_model.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # ORTALAMA
            self.table.setItem(r_idx, 1, item_model)

            # 3. Customer
            self.table.setItem(r_idx, 2, QTableWidgetItem(row.get("username", "-")))

            # 4. Expected Date
            end_date_val = row.get("end_date")
            date_str = end_date_val.strftime("%d.%m.%Y") if end_date_val else "-"
            item_date = QTableWidgetItem(date_str)

            is_late = end_date_val and end_date_val < today
            is_due_today = end_date_val and end_date_val == today

            if is_late:
                item_date.setForeground(Qt.GlobalColor.red)
                f_date = item_date.font()
                f_date.setBold(True)
                item_date.setFont(f_date)

            self.table.setItem(r_idx, 3, item_date)

            # 5. Status (TEXT BASED - STABLE)
            if is_late:
                text = "LATE"
                bg = QBrush(QColor("#fee2e2"))
                fg = QBrush(QColor("#dc2626"))
            elif is_due_today:
                text = "DUE TODAY"
                bg = QBrush(QColor("#ffedd5"))
                fg = QBrush(QColor("#ea580c"))
            else:
                text = "ACTIVE"
                bg = QBrush(QColor("#dcfce7"))
                fg = QBrush(QColor("#166534"))

            status_item = QTableWidgetItem(text)
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            font = status_item.font()
            font.setBold(True)
            font.setPointSize(9)
            status_item.setFont(font)

            #  STYLE-SAFE WAY
            status_item.setData(Qt.ItemDataRole.BackgroundRole, bg)
            status_item.setData(Qt.ItemDataRole.ForegroundRole, fg)

            status_item.setFlags(
                Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
            )

            self.table.setItem(r_idx, 4, status_item)
            self.table.setRowHeight(r_idx, 42)

        self.clear_selection()

    def clear_selection(self):
        self.selected_rental = None
        self.lbl_car_model.setText("Select a rental")
        self.lbl_car_plate.setText("to see details")
        self.lbl_car_img.setText("🚗")

        self.form_container.setEnabled(False)
        self.btn_confirm.setEnabled(False)

        self.lbl_bd_base.setText("-")
        self.lbl_bd_late.setText("-")
        self.lbl_bd_damage.setText("-")
        self.txt_total.setText("0 TL")
        self.inp_damage.clear()
        self.inp_notes.clear()
        self.inp_km.setValue(0)

    def on_row_selected(self):
        selected_items = self.table.selectedItems()
        if not selected_items:
            self.clear_selection()
            return
        row_index = selected_items[0].row()
        item_plate = self.table.item(row_index, 0)
        if not item_plate:
            return

        self.selected_rental = item_plate.data(Qt.ItemDataRole.UserRole)
        self.form_container.setEnabled(True)
        self.btn_confirm.setEnabled(False)

        # Sağ Paneli Güncelle
        self.lbl_car_model.setText(
            f"{self.selected_rental['brand']} {self.selected_rental['model']}"
        )
        self.lbl_car_plate.setText(
            f"Plate: {self.selected_rental['plate_number']} • User: {self.selected_rental['username']}"
        )

        # KM Ayarları
        current_km = self.selected_rental.get("current_car_km", 0)
        start_km = self.selected_rental.get("start_odometer", 0)
        base_km = max(current_km, start_km)

        self.inp_km.setMinimum(0)
        self.inp_km.setValue(base_km)
        self.inp_km.setSpecialValueText(f"Min: {base_km} km")

        end_date = self.selected_rental.get("end_date")
        if end_date:
            q_date = QDate(end_date.year, end_date.month, end_date.day)
            self.date_return.setDate(q_date)
        else:
            self.date_return.setDate(QDate.currentDate())

        self.calculate_total()
        self.validate_km()

    def validate_km(self):
        if not self.selected_rental:
            return

        current_val = self.inp_km.value()
        start_km = self.selected_rental.get("start_odometer", 0)

        if current_val < start_km:
            self.inp_km.setStyleSheet("border: 1px solid #ef4444; color: #ef4444;")
            self.btn_confirm.setEnabled(False)
            self.btn_confirm.setToolTip("End KM cannot be less than Start KM")
        else:
            self.inp_km.setStyleSheet("")
            self.btn_confirm.setEnabled(True)
            self.btn_confirm.setToolTip("")

    def calculate_total(self):
        if not self.selected_rental:
            return

        start_date = self.selected_rental["start_date"]
        expected_date = self.selected_rental.get("end_date")
        return_py_date = self.date_return.date().toPyDate()
        daily_price = float(self.selected_rental["daily_price"])

        if return_py_date < start_date:
            self.txt_total.setText("Invalid Date")
            self.btn_confirm.setEnabled(False)
            return

        self.validate_km()

        base_price = float(self.selected_rental.get("total_price", 0))
        penalty = calculate_late_fee(expected_date, return_py_date, daily_price)

        try:
            d_fee = float(self.inp_damage.text())
        except:
            d_fee = 0.0

        final_total = base_price + penalty + d_fee

        self.lbl_bd_base.setText(f"{int(base_price)} TL")

        if penalty > 0:
            self.lbl_bd_late.setText(f"+{int(penalty)} TL")
            self.lbl_bd_late.setStyleSheet("color: #e74c3c; font-weight: bold;")
        else:
            self.lbl_bd_late.setText("0 TL")
            self.lbl_bd_late.setStyleSheet("color: #64748b;")

        self.lbl_bd_damage.setText(f"+{int(d_fee)} TL")
        self.txt_total.setText(f"{int(final_total)} TL")

    def handle_return(self):
        if not self.selected_rental:
            return

        price_text = self.txt_total.text()
        plate = self.selected_rental["plate_number"]

        confirm = QMessageBox.question(
            self,
            "Confirm Return",
            f"Are you sure you want to return {plate}?\n\nTotal to collect: {price_text}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                d_fee = float(self.inp_damage.text())
            except:
                d_fee = 0.0

            success, info = process_detailed_return(
                rental_id=self.selected_rental["rental_id"],
                car_id=self.selected_rental["car_id"],
                return_date=self.date_return.date().toPyDate(),
                end_km=self.inp_km.value(),
                notes=self.inp_notes.toPlainText(),
                damage_fee=d_fee,
            )

            if success:
                QMessageBox.information(self, "Success", info)
                self.load_rentals()
                if self.on_return_success:
                    self.on_return_success()
            else:
                QMessageBox.critical(self, "Error", info)

    def _make_item(self, text, rental_row, align=None, bold=False):
        item = QTableWidgetItem(text)
        item.setData(Qt.ItemDataRole.UserRole, rental_row)
        if align:
            item.setTextAlignment(align)
        if bold:
            f = item.font()
            f.setBold(True)
            item.setFont(f)
        return item
