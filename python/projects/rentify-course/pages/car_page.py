from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List
import pages.main_window as main_window
from models.car import Car
from services.car_service import add_car as db_add_car, get_all_cars
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
    QLineEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QFormLayout,
    QGroupBox,
    QMessageBox,
    QSpacerItem,
    QSpinBox,
)


class CarsPage(QWidget):
    # Sinyal kaldırıldı (Gerek kalmadı)

    def __init__(self, on_event=None):
        super().__init__()
        self.on_event = on_event

        self._cars: List[main_window.Car] = get_all_cars()
        self._selected_index: Optional[int] = None

        root = QVBoxLayout(self)
        root.setContentsMargins(22, 22, 22, 22)
        root.setSpacing(14)

        title = QLabel("Cars")
        title.setObjectName("pageTitle")

        # ---- Filtre
        filter_box = QGroupBox("Filter")
        f_lay = QHBoxLayout(filter_box)

        self.cb_filter = QComboBox()
        self.cb_filter.addItems(["All", "Available", "Rented", "Maintenance"])
        self.cb_filter.currentTextChanged.connect(self.refresh_table)
        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText("Search (plate / brand / model)...")
        self.le_search.textChanged.connect(self.refresh_table)

        f_lay.addWidget(QLabel("Status:"))
        f_lay.addWidget(self.cb_filter)
        f_lay.addWidget(self.le_search)
        f_lay.addStretch(1)

        # ---- Tablo
        self.table = QTableWidget(0, 6)

        self.table.setHorizontalHeaderLabels(
            ["Plate", "Brand", "Model", "Daily Rate", "Kilometer", "Status"]
        )
        self.table.setSortingEnabled(False)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.itemSelectionChanged.connect(self.on_row_selected)

        # ---- Form
        form_group = QGroupBox("Car Details")
        form = QFormLayout(form_group)

        self.le_plate = QLineEdit()
        self.le_plate.setMaxLength(8)
        self.le_plate.setPlaceholderText("Ex: 34ABC123")

        self.le_brand = QLineEdit()
        self.le_model = QLineEdit()

        self.le_price = QLineEdit()
        self.le_price.setPlaceholderText("Ex: 800")

        self.sb_km = QSpinBox()
        self.sb_km.setRange(0, 999999)  # 0 ile 1 milyon arası
        self.sb_km.setSuffix(" km")
        self.sb_km.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.cb_status = QComboBox()
        self.cb_status.addItems(["Available", "Maintenance"])
        form.addRow("Plate", self.le_plate)
        form.addRow("Brand", self.le_brand)
        form.addRow("Model", self.le_model)
        form.addRow("Daily Rate", self.le_price)
        form.addRow("Kilometer", self.sb_km)
        form.addRow("Status", self.cb_status)

        # ---- Butonlar
        btn_row = QHBoxLayout()

        self.btn_add = QPushButton("Add Car")
        self.btn_add.setObjectName("primaryBtn")
        self.btn_add.clicked.connect(self.add_car)

        self.btn_update = QPushButton("Edit")
        self.btn_update.setObjectName("ghostBtn")
        self.btn_update.clicked.connect(self.update_car)

        self.btn_delete = QPushButton("Delete")
        self.btn_delete.setObjectName("dangerBtn")
        self.btn_delete.clicked.connect(self.delete_car)

        btn_row.addWidget(self.btn_add)
        btn_row.addWidget(self.btn_update)
        btn_row.addWidget(self.btn_delete)
        btn_row.addStretch(1)

        # ---- Layout ekle
        root.addWidget(title)
        root.addWidget(filter_box)
        root.addWidget(self.table)
        root.addWidget(form_group)
        root.addLayout(btn_row)
        root.addStretch(1)

        # İlk açılış: boş liste de olsa tablo boş gösterilir
        self.refresh_table()

    # ---------------- Helpers ----------------
    def clear_form(self):
        self.le_plate.clear()
        self.le_brand.clear()
        self.le_model.clear()
        self.le_price.clear()
        self.cb_status.setCurrentIndex(0)  # müsait
        self.le_plate.setFocus()

    def _validate_form(self) -> Optional[Car]:
        plate = self.le_plate.text().strip().upper()
        brand = self.le_brand.text().strip().upper()
        model = self.le_model.text().strip().upper()
        price_raw = self.le_price.text().replace("TL", "").replace("tl", "").strip()
        status = self.cb_status.currentText().strip().lower()
        kilometer = self.sb_km.value()

        if not plate or not brand or not model or not price_raw:
            QMessageBox.warning(self, "Error!", "All fields are required.")
            return None

        if len(plate) > 8:
            QMessageBox.warning(self, "Error!", "Plate number must be max 8 character.")
            return None

        try:
            price = float(price_raw.replace(",", "."))
        except ValueError:
            QMessageBox.warning(self, "Error!", "Daily rate must be number.")
            return None

        if price <= 0:
            QMessageBox.warning(self, "Error!", "Daily rate must be bigger than 0.")
            return None

        return Car(
            id=None,
            plate_number=plate,
            brand=brand,
            model=model,
            daily_price=price,
            status=status,
            kilometer=kilometer,
        )

    def _current_filter_lower(self) -> str:
        return (
            self.cb_filter.currentText().strip().lower()
        )  # "tümü/müsait/kirada/bakımda"

    # ---------------- UI Events ----------------
    def refresh_table(self):
        # 1. Verileri veritabanından taze çek
        try:
            from services.car_service import get_all_cars

            self._cars = get_all_cars()
        except Exception as e:
            print(f"DB Error: {e}")
            self._cars = []

        # 2. Tabloyu sıfırla ve sıralamayı geçici kapat
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)

        flt = self._current_filter_lower()
        query = self.le_search.text().strip().lower()

        # 3. Filtreleme
        rows = []
        for c in self._cars:
            # Güvenli veri alma
            plate = str(getattr(c, "plate_number", "") or "")
            brand = str(getattr(c, "brand", "") or "")
            model = str(getattr(c, "model", "") or "")
            status = str(getattr(c, "status", "Available") or "Available")

            # Durum Filtresi
            if flt != "all" and status.strip().lower() != flt:
                continue

            # Arama Filtresi
            haystack = f"{plate} {brand} {model}".lower()
            if query and query not in haystack:
                continue

            rows.append(c)

        # 4. Tabloyu Doldur
        for c in rows:
            r = self.table.rowCount()
            self.table.insertRow(r)

            # Verileri hazırla (None kontrolü ile)
            val_plate = str(getattr(c, "plate_number", "") or "-")
            val_brand = str(getattr(c, "brand", "") or "-")
            val_model = str(getattr(c, "model", "") or "-")

            # Fiyat
            try:
                price = int(getattr(c, "daily_price", 0) or 0)
                val_price = f"{price} TL"
            except:
                val_price = "-"

            # KM
            try:
                km = int(getattr(c, "kilometer", 0) or 0)
                val_km = f"{km} km"
            except:
                val_km = "-"

            val_status = str(getattr(c, "status", "") or "Unknown").title()

            # Hücreleri oluştur
            item_plate = QTableWidgetItem(val_plate)
            item_brand = QTableWidgetItem(val_brand)
            item_model = QTableWidgetItem(val_model)
            item_price = QTableWidgetItem(val_price)
            item_km = QTableWidgetItem(val_km)
            item_status = QTableWidgetItem(val_status)

            # Tabloya ekle
            self.table.setItem(r, 0, item_plate)
            self.table.setItem(r, 1, item_brand)
            self.table.setItem(r, 2, item_model)
            self.table.setItem(r, 3, item_price)
            self.table.setItem(r, 4, item_km)
            self.table.setItem(r, 5, item_status)

        self._selected_index = None
        self.table.clearSelection()

    def on_row_selected(self):
        items = self.table.selectedItems()
        if not items:
            self._selected_index = None
            return

        plate_number = self.table.item(self.table.currentRow(), 0).text()

        idx = next(
            (i for i, c in enumerate(self._cars) if c.plate_number == plate_number),
            None,
        )
        self._selected_index = idx

        if idx is None:
            return

        car = self._cars[idx]
        self.le_plate.setText(car.plate_number)
        self.le_brand.setText(car.brand)
        self.le_model.setText(car.model)
        self.le_price.setText(f"{int(car.daily_price)} TL")
        km_val = getattr(car, "kilometer", 0)
        self.sb_km.setValue(km_val)
        self.cb_status.setCurrentText(car.status.title())

    # ---------------- Actions ----------------
    def add_car(self):
        car = self._validate_form()
        if not car:
            return

        if any(c.plate_number == car.plate_number for c in self._cars):
            QMessageBox.warning(self, "Error!", "This plate already exists.")
            return

        try:
            db_add_car(car)
            self._cars = get_all_cars()
            self.cb_filter.setCurrentText("All")
            self.refresh_table()
            QMessageBox.information(self, "Success", "Car added successfully.")
            if self.on_event:
                self.on_event("Car Added!", car.plate_number)
            self.clear_form()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def update_car(self):
        if self._selected_index is None:
            QMessageBox.warning(
                self, "Error!", "Please select a car from the list to edit."
            )
            return

        new_car = self._validate_form()
        if not new_car:
            return

        old_car = self._cars[self._selected_index]

        # plaka değiştiyse, başka araçla çakışmasın
        for i, c in enumerate(self._cars):
            if i != self._selected_index and c.plate_number == new_car.plate_number:
                QMessageBox.warning(self, "Error!", "This plate is already in use.")
                return

        #  ID'Yİ KORU
        new_car.id = old_car.id

        try:
            from services.car_service import update_car as db_update_car

            db_update_car(new_car)  # DB UPDATE

            self._cars[self._selected_index] = new_car
            self.cb_filter.setCurrentText("All")
            self.refresh_table()

            QMessageBox.information(
                self, "Success", "Car details updated successfully."
            )
            if self.on_event:
                self.on_event("Car Updated", new_car.plate_number)

            self.clear_form()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def delete_car(self):
        if self._selected_index is None:
            QMessageBox.warning(
                self, "Error!", "Please select a car from the list to delete."
            )
            return

        car = self._cars[self._selected_index]

        reply = QMessageBox.question(
            self,
            "Confirmation",
            f"Are you sure you want to delete the car with license plate {car.plate_number}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            from services.car_service import delete_car as db_delete_car

            db_delete_car(car.id)  #  DB'DEN SİL
            self._cars.pop(self._selected_index)

            self.cb_filter.setCurrentText("All")
            self.refresh_table()

            QMessageBox.information(self, "Success", "Car deleted.")
            if self.on_event:
                self.on_event("Car Deleted", car.plate_number)

            self.clear_form()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    def reload_cars_from_db(self):
        from services.car_service import get_all_cars

        self._cars = get_all_cars()

        self.cb_filter.setCurrentIndex(0)
        self.le_search.clear()
        self.refresh_table()

    def clear_form(self):
        self.le_plate.clear()
        self.le_brand.clear()
        self.le_model.clear()
        self.le_price.clear()
        self.cb_status.setCurrentIndex(0)
        self.sb_km.setValue(0)

        self._selected_index = None
        self.table.clearSelection()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        clicked = self.childAt(event.pos())

        # Eğer tıklanan yer TABLO VE seçili satır varsa -> temizleme
        if clicked == self.table and self.table.selectedItems():
            return

        # Diğer tüm durumlarda -> formu temizle
        self.clear_form()
