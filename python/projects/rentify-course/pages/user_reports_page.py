from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QSizePolicy,
)
from PyQt6.QtCore import Qt, QPropertyAnimation

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# Sadece genel kiralama verisini çekip kullanıcıya göre filtreleyeceğiz
from services.report_service import get_recent_rentals


# =====================================================
# BASE CHART
# =====================================================
class BaseChart(FigureCanvasQTAgg):
    def __init__(self, width=4, height=3):
        self.fig = Figure(figsize=(width, height))
        self.fig.patch.set_facecolor("white")
        super().__init__(self.fig)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


# =====================================================
# USER REPORTS PAGE (KULLANICI RAPORLARI)
# =====================================================
class UserReportsPage(QWidget):
    def __init__(self, current_user):
        super().__init__()
        self.setObjectName("UserReportsPageWidget")
        self.current_user = current_user

        # 1. Arayüzü Kur
        self.init_ui()

        # 2. Verileri Yükle
        self.load_data()

    # -------------------------------------------------
    # UI SETUP
    # -------------------------------------------------
    def init_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(25, 25, 25, 25)
        main.setSpacing(25)

        title = QLabel(f"My Reports - {self.current_user.username}")
        title.setObjectName("pageTitle")
        main.addWidget(title)

        # ==============================
        # KPI CARDS
        # ==============================
        self.cards_layout = QHBoxLayout()

        self.card_total = self.create_card("My Rentals", "0")
        self.card_active = self.create_card("Active Rental", "No")
        self.card_spent = self.create_card("Total Spent", "₺0")
        self.card_late = self.create_card("Late Rentals", "0")

        self.cards_layout.addWidget(self.card_total)
        self.cards_layout.addWidget(self.card_active)
        self.cards_layout.addWidget(self.card_spent)
        self.cards_layout.addWidget(self.card_late)

        main.addLayout(self.cards_layout)

        # ==============================
        # CHARTS
        # ==============================
        charts = QGridLayout()
        charts.setSpacing(20)

        self.pie_chart = BaseChart()
        self.line_chart = BaseChart(width=8, height=3)

        charts.addWidget(self.wrap_chart("My Rental Status", self.pie_chart), 0, 0)
        charts.addWidget(self.wrap_chart("My Monthly Spending", self.line_chart), 1, 0)

        main.addLayout(charts)

    # -------------------------------------------------
    # LOAD DATA
    # -------------------------------------------------
    def load_data(self):
        if not self.current_user:
            return

        self.animate_refresh()

        try:
            # Tüm kiralamaları çek
            all_rentals = get_recent_rentals(1000)

            # Sadece BU KULLANICIYA ait olanları filtrele
            my_rentals = [
                r
                for r in all_rentals
                if r.get("username") == self.current_user.username
            ]

            total = len(my_rentals)
            active = sum(1 for r in my_rentals if r.get("actual_return_date") is None)

            # Harcanan Tutar
            spent = 0
            for r in my_rentals:
                try:
                    spent += float(r.get("total_price", 0))
                except:
                    pass

            # Kartları Güncelle
            self.set_card(self.card_total, total)
            self.set_card(self.card_active, "Yes" if active else "No")
            self.set_card(self.card_spent, f"₺{int(spent)}")
            self.set_card(self.card_late, 0)  # Şimdilik 0

            # Grafikleri Çiz
            self.draw_pie(my_rentals)
            self.draw_line(my_rentals)

        except Exception as e:
            print(f"User Report Error: {e}")

    # -------------------------------------------------
    # HELPER FUNCTIONS
    # -------------------------------------------------
    def create_card(self, title, value):
        card = QFrame()
        card.setObjectName("modernCard")
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        l_title = QLabel(title)
        l_title.setObjectName("cardTitle")
        l_val = QLabel(value)
        l_val.setObjectName("cardValue")

        layout.addWidget(l_title)
        layout.addWidget(l_val)
        return card

    def set_card(self, card, value):
        card.layout().itemAt(1).widget().setText(str(value))

    def wrap_chart(self, title, chart):
        card = QFrame()
        card.setObjectName("modernCard")
        lay = QVBoxLayout(card)
        lbl = QLabel(title)
        lbl.setStyleSheet("font-weight: bold; font-size: 14px; color: #334155;")
        lay.addWidget(lbl)
        lay.addWidget(chart)
        return card

    def draw_pie(self, rentals):
        self.pie_chart.fig.clear()
        ax = self.pie_chart.fig.add_subplot(111)

        active = sum(1 for r in rentals if r.get("actual_return_date") is None)
        returned = len(rentals) - active

        if len(rentals) == 0:
            ax.text(0.5, 0.5, "No Data", ha="center", va="center")
            ax.axis("off")
        else:
            ax.pie(
                [active, returned],
                labels=["Active", "Returned"],
                autopct="%1.1f%%",
                startangle=90,
                colors=["#3b82f6", "#10b981"],
            )
            ax.set_title("Status")

        self.pie_chart.draw()

    def draw_line(self, rentals):
        self.line_chart.fig.clear()
        ax = self.line_chart.fig.add_subplot(111)

        monthly = {}
        for r in rentals:
            d = r.get("start_date")
            if d:
                k = str(d)[:7]  # YYYY-MM
                try:
                    p = float(r.get("total_price", 0))
                    monthly[k] = monthly.get(k, 0) + p
                except:
                    pass

        months = sorted(monthly.keys())
        vals = [monthly[m] for m in months]

        if not months:
            ax.text(0.5, 0.5, "No Spending Data", ha="center", va="center")
            ax.axis("off")
        else:
            ax.plot(months, vals, marker="o", color="#f59e0b")
            ax.set_ylabel("Spent (₺)")
            ax.grid(True, alpha=0.3)

        self.line_chart.draw()

    def animate_refresh(self):
        self.fade = QPropertyAnimation(self, b"windowOpacity")
        self.fade.setDuration(300)
        self.fade.setStartValue(0.7)
        self.fade.setEndValue(1.0)
        self.fade.start()
