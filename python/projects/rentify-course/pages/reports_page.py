# pages/reports_page.py
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QSizePolicy,
)
from PyQt6.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from services.report_service import (
    get_summary_report,
    get_monthly_revenue,
    get_recent_rentals,
    get_overdue_rentals,
)


# =====================================================
# BASE CHART – ABSOLUTELY FIXED HEIGHT
# =====================================================
class BaseChart(FigureCanvasQTAgg):
    def __init__(self, fixed_height: int):
        self.fig = Figure(figsize=(5, 3))
        self.fig.patch.set_facecolor("white")
        super().__init__(self.fig)

        #  MUTLAK SABİTLEME (QT ARTIK DOKUNAMAZ)
        self.setMinimumHeight(fixed_height)
        self.setMaximumHeight(fixed_height)
        self.setFixedHeight(fixed_height)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )


# =====================================================
# REPORTS PAGE
# =====================================================
class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("ReportsPageWidget")

        self.init_ui()
        self.load_data()

    # -------------------------------------------------
    # UI SETUP
    # -------------------------------------------------
    def init_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(25, 25, 25, 25)
        main.setSpacing(25)

        # Title
        title = QLabel("Reports & Analytics")
        title.setObjectName("pageTitle")
        main.addWidget(title)

        # ==============================
        # KPI CARDS
        # ==============================
        stats = QHBoxLayout()

        self.card_total_cars = self.create_stat_card("Total Cars", "0")
        self.card_rented = self.create_stat_card("Rented Cars", "0")
        self.card_rentals = self.create_stat_card("Total Rentals", "0")
        self.card_income = self.create_stat_card("Total Revenue", "₺0")

        for card in (
            self.card_total_cars,
            self.card_rented,
            self.card_rentals,
            self.card_income,
        ):
            stats.addWidget(card)

        main.addLayout(stats)

        # ==============================
        # CHARTS GRID
        # ==============================
        charts = QGridLayout()
        charts.setSpacing(20)

        #  HEIGHT’LER BİLEREK AYRI AYRI
        self.line_chart = BaseChart(fixed_height=180)
        self.pie_chart = BaseChart(fixed_height=160)
        self.bar_chart = BaseChart(fixed_height=160)

        charts.addWidget(
            self.wrap_chart("Monthly Revenue", self.line_chart), 0, 0, 1, 2
        )
        charts.addWidget(
            self.wrap_chart("Rental Status Distribution", self.pie_chart), 1, 0
        )
        charts.addWidget(self.wrap_chart("Most Rented Brands", self.bar_chart), 1, 1)

        main.addLayout(charts)

    # -------------------------------------------------
    # DATA
    # -------------------------------------------------
    def load_data(self):
        summary = get_summary_report()

        self.set_card_value(self.card_total_cars, summary["total_cars"])
        self.set_card_value(self.card_rented, summary["rented_cars"])
        self.set_card_value(self.card_rentals, summary["total_rentals"])
        self.set_card_value(self.card_income, f"₺{int(summary['total_income'])}")

        self.draw_monthly_revenue()
        self.draw_status_pie()
        self.draw_brand_bar()

    # -------------------------------------------------
    # KPI CARD
    # -------------------------------------------------
    def create_stat_card(self, title: str, value: str) -> QFrame:
        card = QFrame()
        card.setObjectName("modernCard")

        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_title = QLabel(title)
        lbl_title.setObjectName("cardTitle")
        lbl_value = QLabel(value)
        lbl_value.setObjectName("cardValue")

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)
        return card

    def set_card_value(self, card: QFrame, value):
        card.layout().itemAt(1).widget().setText(str(value))

    # -------------------------------------------------
    # CHART WRAPPER (NO FIXED HEIGHT HERE)
    # -------------------------------------------------
    def wrap_chart(self, title: str, chart: QWidget) -> QFrame:
        card = QFrame()
        card.setObjectName("modernCard")

        layout = QVBoxLayout(card)
        layout.setSpacing(10)

        lbl = QLabel(title)
        lbl.setStyleSheet("font-weight: bold; font-size: 14px; color: #334155;")

        layout.addWidget(lbl)
        layout.addWidget(chart)

        return card

    # -------------------------------------------------
    # LINE CHART (CANNOT MOVE ANYMORE)
    # -------------------------------------------------
    def draw_monthly_revenue(self):
        fig = self.line_chart.fig
        fig.clear()

        ax = fig.add_subplot(111)

        data = get_monthly_revenue()
        months = [r["month"] for r in reversed(data)]
        revenue = [r["revenue"] for r in reversed(data)]

        ax.plot(months, revenue, marker="o")
        ax.set_ylabel("Revenue")
        ax.set_xlabel("Month")

        ax.tick_params(axis="x", rotation=30)
        ax.grid(True, alpha=0.3)

        self.line_chart.draw()

    # -------------------------------------------------
    # PIE CHART
    # -------------------------------------------------
    def draw_status_pie(self):
        fig = self.pie_chart.fig
        fig.clear()
        ax = fig.add_subplot(111)

        recent = get_recent_rentals(500)

        active = sum(1 for r in recent if r["actual_return_date"] is None)
        returned = sum(1 for r in recent if r["actual_return_date"] is not None)
        total = active + returned

        if total == 0:
            ax.text(
                0.5,
                0.5,
                "No rental data",
                ha="center",
                va="center",
                fontsize=12,
                color="#64748b",
            )
            ax.axis("off")
        else:
            ax.pie(
                [active, returned],
                labels=["Active", "Returned"],
                autopct="%1.0f%%",
                startangle=90,
            )
            ax.axis("equal")

        self.pie_chart.draw()

    # -------------------------------------------------
    # BAR CHART
    # -------------------------------------------------
    def draw_brand_bar(self):
        fig = self.bar_chart.fig
        fig.clear()

        ax = fig.add_subplot(111)

        rentals = get_recent_rentals(500)
        brand_count = {}

        for r in rentals:
            brand_count[r["brand"]] = brand_count.get(r["brand"], 0) + 1

        ax.bar(brand_count.keys(), brand_count.values())
        ax.set_ylabel("Rentals")
        ax.set_xlabel("Brand")
        ax.tick_params(axis="x", rotation=30)

        self.bar_chart.draw()
