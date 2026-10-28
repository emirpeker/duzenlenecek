import os
import random
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QPushButton,
    QSizePolicy,
    QProgressBar,
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from services.car_service import get_all_cars
from services.rental_service import get_all_rentals, get_active_rentals

try:
    from services.customer_service import get_all_customers
except ImportError:

    def get_all_customers():
        return []


class DashboardPage(QWidget):
    # Sinyal artık opsiyonel olarak bir string (plaka) taşıyabilir
    request_rental_page = pyqtSignal(str)
    request_returns_page = pyqtSignal()

    def __init__(self, current_user):
        super().__init__()
        self.current_user = current_user
        self.stat_cards = {}
        self.dashboard_table = None
        self.loyalty_widget = None
        self.recommendation_widget = None
        self.dynamic_banner = None

        self.init_ui()
        self.load_data()

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)

        # --- HEADER ---
        header_layout = QHBoxLayout()
        display_name = str(
            self.current_user.name
            if self.current_user.name
            else self.current_user.username
        ).title()

        welcome_text = (
            f"Welcome back, Admin!"
            if self.current_user.role == "admin"
            else f"Hello, {display_name}!"
        )
        sub_text = (
            "Fleet Management Overview"
            if self.current_user.role == "admin"
            else "Ready for your next trip?"
        )

        title_box = QVBoxLayout()
        lbl_welcome = QLabel(welcome_text)
        lbl_welcome.setStyleSheet("font-size: 32px; font-weight: 800; color: #1e293b;")
        lbl_sub = QLabel(sub_text)
        lbl_sub.setStyleSheet("font-size: 16px; color: #64748b;")

        title_box.addWidget(lbl_welcome)
        title_box.addWidget(lbl_sub)
        header_layout.addLayout(title_box)
        header_layout.addStretch()
        self.main_layout.addLayout(header_layout)

        # --- DASHBOARD CONTENT ---
        if self.current_user.role == "admin":
            self.setup_admin_dashboard()
        else:
            self.setup_user_dashboard()

    def setup_admin_dashboard(self):
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(15)

        self.stat_cards["total_cars"] = self.create_modern_card(
            "car.png", "Fleet", "0", "#3b82f6"
        )
        self.stat_cards["available"] = self.create_modern_card(
            "check.png", "Available", "0", "#22c55e"
        )
        self.stat_cards["rented"] = self.create_modern_card(
            "key.png", "Active", "0", "#f59e0b"
        )
        self.stat_cards["earnings"] = self.create_modern_card(
            "wallet.png", "Revenue", "0", "#8b5cf6"
        )
        self.stat_cards["total_users"] = self.create_modern_card(
            "users.png", "Customers", "0", "#ec4899"
        )

        stats_layout.addWidget(self.stat_cards["total_cars"])
        stats_layout.addWidget(self.stat_cards["available"])
        stats_layout.addWidget(self.stat_cards["rented"])
        stats_layout.addWidget(self.stat_cards["earnings"])
        stats_layout.addWidget(self.stat_cards["total_users"])
        self.main_layout.addLayout(stats_layout)

        self.main_layout.addSpacing(10)
        lbl_recent = QLabel("Recent Fleet Activity")
        lbl_recent.setStyleSheet("font-size: 18px; font-weight: 700; color: #334155;")
        self.main_layout.addWidget(lbl_recent)

        self.dashboard_table = self.create_modern_table(
            ["Plate", "Model", "Customer", "Date", "Status"]
        )
        self.main_layout.addWidget(self.dashboard_table)

    def setup_user_dashboard(self):
        # 1. KARTLAR
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(15)

        self.stat_cards["my_active"] = self.create_modern_card(
            "key.png", "My Car", "0", "#f59e0b"
        )
        self.stat_cards["total_rentals"] = self.create_modern_card(
            "car.png", "History", "0", "#3b82f6"
        )
        self.stat_cards["total_spent"] = self.create_modern_card(
            "wallet.png", "Spent", "0", "#10b981"
        )

        stats_layout.addWidget(self.stat_cards["my_active"])
        stats_layout.addWidget(self.stat_cards["total_rentals"])
        stats_layout.addWidget(self.stat_cards["total_spent"])
        self.main_layout.addLayout(stats_layout)

        # 2. LOYALTY WIDGET
        self.loyalty_widget = self.create_loyalty_widget()
        self.main_layout.addWidget(self.loyalty_widget)

        # 3. DİNAMİK BANNER
        self.dynamic_banner = QFrame()
        self.main_layout.addWidget(self.dynamic_banner)

        # 4. AKTİF KİRALAMA TABLOSU
        self.lbl_active_title = QLabel("Your Active Rental Details")
        self.lbl_active_title.setStyleSheet(
            "font-size: 18px; font-weight: 700; color: #334155; margin-top:10px;"
        )
        self.main_layout.addWidget(self.lbl_active_title)

        self.dashboard_table = self.create_modern_table(
            ["Plate", "Car Model", "Start Date", "Return Date", "Total Price"]
        )
        self.dashboard_table.setFixedHeight(100)
        self.main_layout.addWidget(self.dashboard_table)

        # 5. ÖNERİLEN ARAÇLAR
        self.recommendation_wrapper = QWidget()  # Gizleyip açmak için wrapper
        rec_layout = QVBoxLayout(self.recommendation_wrapper)
        rec_layout.setContentsMargins(0, 10, 0, 0)

        self.lbl_rec = QLabel("Recommended For You 🌟")
        self.lbl_rec.setStyleSheet("font-size: 18px; font-weight: 700; color: #334155;")
        rec_layout.addWidget(self.lbl_rec)

        self.recommendation_widget = QWidget()
        rec_layout.addWidget(self.recommendation_widget)

        self.main_layout.addWidget(self.recommendation_wrapper)

        # Esnek boşluk ekle ki yukarı yaslansın
        self.main_layout.addStretch()

    # --- WIDGET OLUŞTURUCULAR ---
    def create_loyalty_widget(self):
        widget = QFrame()
        widget.setObjectName("loyaltyCard")
        widget.setStyleSheet(
            """
            QFrame#loyaltyCard {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:1 #f8fafc);
                border-radius: 16px; 
                border: 1px solid #e2e8f0;
            }
        """
        )
        widget.setFixedHeight(100)

        layout = QHBoxLayout(widget)
        layout.setContentsMargins(25, 15, 25, 15)
        layout.setSpacing(20)

        self.lbl_tier_icon = QLabel("🥉")
        self.lbl_tier_icon.setStyleSheet("font-size: 48px; background: transparent;")
        self.lbl_tier_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 2. ORTA: Bilgiler
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)

        # Üst Başlık (Tier Name)
        self.lbl_loyalty_tier = QLabel("Bronze Member")
        self.lbl_loyalty_tier.setStyleSheet(
            "font-size: 18px; font-weight: 800; color: #334155; background: transparent;"
        )

        # Alt Başlık (Benefit / Motivation)
        self.lbl_tier_benefit = QLabel("Current Benefit: Standard Support")
        self.lbl_tier_benefit.setStyleSheet(
            "font-size: 13px; color: #64748b; font-style: italic; background: transparent;"
        )

        info_layout.addWidget(self.lbl_loyalty_tier)
        info_layout.addWidget(self.lbl_tier_benefit)

        # 3. SAĞ: Progress Bar ve Sayaç
        progress_layout = QVBoxLayout()
        progress_layout.setSpacing(5)

        # "2 rentals left" yazısı (Sağa dayalı)
        self.lbl_next_goal_text = QLabel("Next: Silver (5 rentals)")
        self.lbl_next_goal_text.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.lbl_next_goal_text.setStyleSheet(
            "font-size: 12px; font-weight: bold; color: #6366f1; background: transparent;"
        )

        # Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(
            """
            QProgressBar {
                border: none; background-color: #e2e8f0; border-radius: 8px; height: 12px; text-align: center;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6366f1, stop:1 #a855f7);
                border-radius: 8px;
            }
        """
        )
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(12)

        progress_layout.addWidget(self.lbl_next_goal_text)
        progress_layout.addWidget(self.progress_bar)

        layout.addWidget(self.lbl_tier_icon)
        layout.addLayout(info_layout, stretch=1)  # Yazılar esnesin
        layout.addLayout(progress_layout, stretch=1)  # Bar esnesin

        return widget

    def update_loyalty(self, total_rentals):
        BRONZE_LIMIT = 5
        SILVER_LIMIT = 15
        GOLD_LIMIT = 30
        if total_rentals < BRONZE_LIMIT:
            # BRONZE SEVİYESİ
            tier_name = "Bronze Member"
            icon = "🥉"
            color = "#cd7f32"  # Bronz Rengi
            benefit = "Start your journey!"

            # Hedef Hesaplama
            current_goal = BRONZE_LIMIT
            prev_goal = 0
            next_tier_name = "Silver"

        elif total_rentals < SILVER_LIMIT:
            # SILVER SEVİYESİ
            tier_name = "Silver Member"
            icon = "🥈"
            color = "#64748b"  # Gümüş Rengi
            benefit = "Perk: 5% Discount applied"

            current_goal = SILVER_LIMIT
            prev_goal = BRONZE_LIMIT
            next_tier_name = "Gold"

        elif total_rentals < GOLD_LIMIT:
            # GOLD SEVİYESİ
            tier_name = "Gold Member"
            icon = "🥇"
            color = "#eab308"  # Altın Rengi
            benefit = "Perk: 10% Discount + Priority Support"

            current_goal = GOLD_LIMIT
            prev_goal = SILVER_LIMIT
            next_tier_name = "Diamond"  # Hayali bir sonraki seviye

        else:
            # PLATINUM / MAX SEVİYE
            tier_name = "Diamond Driver 💎"
            icon = "💎"
            color = "#0ea5e9"  # Elmas Mavisi
            benefit = "Legendary Status: 15% Discount"

            current_goal = 100  # Sembolik
            prev_goal = GOLD_LIMIT
            next_tier_name = "Infinity"

        range_span = current_goal - prev_goal
        current_progress_in_tier = total_rentals - prev_goal

        if total_rentals >= GOLD_LIMIT:
            percentage = 100
            goal_text = "Max Level Reached!"
        else:
            percentage = int((current_progress_in_tier / range_span) * 100)
            left = current_goal - total_rentals
            goal_text = f"{left} rentals to {next_tier_name}"

        # Arayüzü Güncelle
        self.lbl_tier_icon.setText(icon)
        self.lbl_loyalty_tier.setText(tier_name)
        self.lbl_loyalty_tier.setStyleSheet(
            f"font-size: 18px; font-weight: 800; color: {color}; background: transparent;"
        )

        self.lbl_tier_benefit.setText(benefit)

        self.lbl_next_goal_text.setText(goal_text)
        self.progress_bar.setValue(min(percentage, 100))

    def update_dynamic_banner(self, has_active_rental):
        if self.dynamic_banner.layout():
            QWidget().setLayout(self.dynamic_banner.layout())

        layout = QHBoxLayout(self.dynamic_banner)
        layout.setContentsMargins(20, 20, 20, 20)

        text_layout = QVBoxLayout()
        btn = QPushButton()
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedSize(140, 40)

        if has_active_rental:
            self.dynamic_banner.setStyleSheet(
                "background-color: #dcfce7; border-radius: 12px; border: 1px solid #22c55e;"
            )
            title = QLabel("Current Journey Active 🚗")
            title.setStyleSheet(
                "font-size: 18px; font-weight: bold; color: #166534; background: transparent; border: none;"
            )
            desc = QLabel("Drive safe! Don't forget to check return date.")
            desc.setStyleSheet("color: #15803d; background: transparent; border: none;")

            btn.setText("Manage Rental")
            btn.setStyleSheet(
                "background-color: #166534; color: white; border-radius: 6px; font-weight: bold;"
            )
            btn.clicked.connect(lambda: self.request_returns_page.emit())
            # Ekran kaymasını önlemek için Önerileri Gizle
            if hasattr(self, "recommendation_wrapper"):
                self.recommendation_wrapper.hide()

        else:
            # Mavi Banner
            self.dynamic_banner.setStyleSheet(
                "background-color: #2563EB; border-radius: 12px;"
            )
            title = QLabel("Ready for a new adventure?")
            title.setStyleSheet(
                "font-size: 18px; font-weight: bold; color: white; background: transparent; border: none;"
            )
            desc = QLabel("Check out our premium fleet available today.")
            desc.setStyleSheet("color: #bfdbfe; background: transparent; border: none;")

            btn.setText("Rent Now ➔")
            btn.setStyleSheet(
                "background-color: white; color: #2563EB; border-radius: 6px; font-weight: bold;"
            )
            btn.clicked.connect(
                lambda: self.request_rental_page.emit("")
            )  # Boş string = sadece sayfayı aç

            # Kiralama yoksa Önerileri Göster
            if self.recommendation_wrapper:
                self.recommendation_wrapper.show()

        text_layout.addWidget(title)
        text_layout.addWidget(desc)
        layout.addLayout(text_layout)
        layout.addStretch()
        layout.addWidget(btn)

    def update_recommendations(self):
        # Eğer gizliyse boşuna işlem yapma
        if self.recommendation_wrapper and self.recommendation_wrapper.isHidden():
            return

        all_cars = get_all_cars()
        available_cars = [c for c in all_cars if c.status == "available"]
        recs = random.sample(available_cars, min(3, len(available_cars)))

        if self.recommendation_widget.layout():
            QWidget().setLayout(self.recommendation_widget.layout())

        grid = QHBoxLayout(self.recommendation_widget)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(15)

        if not recs:
            grid.addWidget(QLabel("No cars available right now :("))
            return

        for car in recs:
            card = QFrame()
            card.setStyleSheet(
                """
                QFrame { background-color: white; border: 1px solid #e2e8f0; border-radius: 12px; }
                QFrame:hover { border: 1px solid #3b82f6; }
            """
            )
            card.setFixedWidth(220)
            cl = QVBoxLayout(card)
            cl.setContentsMargins(15, 15, 15, 15)

            img_lbl = QLabel("🚘")
            img_lbl.setStyleSheet(
                "font-size: 30px; background: #f1f5f9; border-radius: 8px; padding: 5px; border:none;"
            )
            img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

            lbl_model = QLabel(f"{car.brand} {car.model}")
            lbl_model.setStyleSheet(
                "font-weight: bold; font-size: 14px; color: #334155; margin-top: 5px; border:none; background:transparent;"
            )

            lbl_price = QLabel(f"{int(car.daily_price)} TL / day")
            lbl_price.setStyleSheet(
                "color: #2563eb; font-weight: bold; border:none; background:transparent;"
            )

            btn_mini = QPushButton("Rent This")
            btn_mini.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_mini.setStyleSheet(
                """
                QPushButton { background-color: #3b82f6; color: white; border-radius: 6px; padding: 6px; font-weight: bold; }
                QPushButton:hover { background-color: #2563eb; }
            """
            )

            btn_mini.clicked.connect(
                lambda checked, plate=car.plate_number: self.request_rental_page.emit(
                    plate
                )
            )

            cl.addWidget(img_lbl)
            cl.addWidget(lbl_model)
            cl.addWidget(lbl_price)
            cl.addWidget(btn_mini)
            grid.addWidget(card)
        grid.addStretch()

    def create_modern_card(self, icon_name, title, value, color_hex):
        card = QFrame()
        card.setObjectName("modernCard")
        card.setStyleSheet(
            f"QFrame#modernCard {{ border-left: 5px solid {color_hex}; }}"
        )
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        card.setFixedHeight(90)

        layout = QHBoxLayout(card)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(12)

        icon_path = f"ui/icons/{icon_name}"
        lbl_icon = QLabel()
        lbl_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path)
            lbl_icon.setPixmap(
                pixmap.scaled(
                    28,
                    28,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            lbl_icon.setStyleSheet(
                f"background-color: {color_hex}15; border-radius: 8px; padding: 6px;"
            )
        else:
            fallback = title[0]
            lbl_icon.setText(fallback)
            lbl_icon.setStyleSheet(
                f"font-size: 20px; background-color: {color_hex}15; color: {color_hex}; border-radius: 8px; padding: 5px; min-width: 36px; qproperty-alignment: AlignCenter;"
            )

        text_layout = QVBoxLayout()
        text_layout.setSpacing(0)

        lbl_title = QLabel(title)
        lbl_title.setObjectName("cardTitle")
        lbl_title.setStyleSheet(
            "font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase; border:none; background:transparent;"
        )

        lbl_value = QLabel(value)
        lbl_value.setObjectName("cardValue")
        lbl_value.setStyleSheet(
            "font-size: 22px; font-weight: 800; color: #1e293b; border:none; background:transparent;"
        )

        card.value_lbl = lbl_value
        text_layout.addWidget(lbl_title)
        text_layout.addWidget(lbl_value)
        layout.addWidget(lbl_icon)
        layout.addLayout(text_layout)
        layout.addStretch()
        return card

    def create_modern_table(self, columns):
        table = QTableWidget()
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.ResizeToContents
        )
        table.setSortingEnabled(False)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        table.setAlternatingRowColors(True)
        table.setStyleSheet("QTableWidget::item { padding-left: 10px; }")
        return table

    def format_tl(self, x: float) -> str:
        s = f"{int(x):,}".replace(",", ".")
        return f"{s} TL"

    def update_card(self, key, value):
        if key in self.stat_cards:
            self.stat_cards[key].value_lbl.setText(str(value))

    def load_data(self):
        if self.current_user.role == "admin":
            self.load_admin_data()
        else:
            self.load_user_data()

    def load_admin_data(self):
        all_cars = get_all_cars()
        total = len(all_cars)
        avail = sum(1 for c in all_cars if c.status == "available")
        rented = sum(1 for c in all_cars if c.status == "rented")

        all_rentals = get_all_rentals()
        earn = sum(float(r["total_price"]) for r in all_rentals if r.get("total_price"))
        try:
            cust = len(get_all_customers())
        except:
            cust = 0

        self.update_card("total_cars", total)
        self.update_card("available", avail)
        self.update_card("rented", rented)
        self.update_card("earnings", self.format_tl(earn))
        self.update_card("total_users", cust)

        # get_all_rentals() zaten DESC geliyorsa ilk 8 yeter
        recent = all_rentals[:8]

        self.dashboard_table.setRowCount(0)
        for r in recent:
            idx = self.dashboard_table.rowCount()
            self.dashboard_table.insertRow(idx)

            self.dashboard_table.setItem(idx, 0, QTableWidgetItem(r["plate_number"]))
            self.dashboard_table.setItem(
                idx, 1, QTableWidgetItem(f"{r.get('brand','')} {r.get('model','')}")
            )
            self.dashboard_table.setItem(
                idx, 2, QTableWidgetItem(r.get("username", ""))
            )

            date_str = (
                r["start_date"].strftime("%d.%m.%Y") if r.get("start_date") else "-"
            )
            self.dashboard_table.setItem(idx, 3, QTableWidgetItem(date_str))

            status = "Active" if r.get("actual_return_date") is None else "Completed"
            status_item = QTableWidgetItem(status)
            status_item.setForeground(
                Qt.GlobalColor.darkGreen if status == "Active" else Qt.GlobalColor.gray
            )
            self.dashboard_table.setItem(idx, 4, status_item)

    def load_user_data(self):
        user_id = self.current_user.id
        my_active = get_active_rentals(user_id, "user")
        all_rentals = get_all_rentals()
        my_history = [r for r in all_rentals if r["user_id"] == user_id]
        spent = sum(float(r["total_price"]) for r in my_history if r.get("total_price"))

        self.update_card("my_active", len(my_active))
        self.update_card("total_rentals", len(my_history))
        self.update_card("total_spent", self.format_tl(spent))

        self.update_loyalty(len(my_history))
        self.update_dynamic_banner(has_active_rental=len(my_active) > 0)
        self.update_recommendations()

        if not my_active:
            self.dashboard_table.hide()
            self.lbl_active_title.hide()
        else:
            self.lbl_active_title.show()
            self.dashboard_table.show()
            self.dashboard_table.setRowCount(0)
            for r in my_active:
                idx = self.dashboard_table.rowCount()
                self.dashboard_table.insertRow(idx)
                self.dashboard_table.setItem(
                    idx, 0, QTableWidgetItem(r["plate_number"])
                )
                self.dashboard_table.setItem(
                    idx, 1, QTableWidgetItem(f"{r['brand']} {r['model']}")
                )
                s_date = (
                    r["start_date"].strftime("%d.%m.%Y") if r["start_date"] else "-"
                )
                self.dashboard_table.setItem(idx, 2, QTableWidgetItem(s_date))
                e_date = r["end_date"].strftime("%d.%m.%Y") if r["end_date"] else "-"
                self.dashboard_table.setItem(idx, 3, QTableWidgetItem(e_date))
                total_p = r.get("total_price", 0)
                price = int(float(total_p))
                self.dashboard_table.setItem(idx, 4, QTableWidgetItem(f"{price} TL"))
