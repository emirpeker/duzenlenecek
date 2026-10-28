# ui/stylesheet.py

# ============================================================
# 1. ANA UYGULAMA GENEL STİLİ (MAIN WINDOW)
# ============================================================
APP_STYLE = """
/* ===== GENEL SIFIRLAMA (NORMALIZE) ===== */
* {
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
    font-weight: normal; /* Her şeyi varsayılan olarak ince yap */
}

QMainWindow {
    background-color: #F8FAFC;
}

QWidget {
    color: #0F172A; 
}

/* ===== SIDEBAR ===== */
#sidebar {
    background-color: #0b418d;
}

#sideTitle {
    color: #F9FAFB;
    font-size: 22px;
    font-weight: 700;
    padding: 10px 6px;
}

#sideSub {
    color: #CBD5E1;
    font-size: 12px;
    padding-left: 6px;
    padding-bottom: 10px;
}

/* Sidebar butonları */
#sideBtn {
    background-color: transparent;
    color: #E5E7EB;
    border: none;
    border-radius: 10px;
    padding: 10px 14px;
    text-align: left;
    font-size: 14px;
    font-weight: normal;
}

#sideBtn:hover {
    background-color: #374151;
    color: #FFFFFF;
}

#sideBtn:pressed {
    background-color: #111827;
}

#sideBtn[active="true"] {
    background-color: #2563EB;
    color: #FFFFFF;
    font-weight: 600;
}

/* ===== CONTENT AREA (BAŞLIKLAR) ===== */
#pageTitle {
    font-size: 26px;
    font-weight: 700;
    color: #0F172A;
    background-color: transparent;
}

#pageInfo {
    font-size: 14px;
    color: #334155;
    background-color: transparent;
}

#sectionTitle {
    font-size: 16px;
    font-weight: 700;
    color: #0F172A;
    margin-top: 6px;
    background-color: transparent;
}

/* Düz Etiketler (Labels) */
QLabel {
    font-size: 14px;
    font-weight: normal;
    color: #333333;
    border: none;
}

/* ===== FORM & INPUT (GENEL) ===== */
QGroupBox {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    margin-top: 12px;
    font-weight: 600; 
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 14px;
    padding: 0 6px;
    color: #0F172A;
}

QLineEdit, QPlainTextEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QDateTimeEdit {
    background-color: #FFFFFF;
    color: #0F172A;
    border: 1px solid #CBD5E1;
    border-radius: 10px;
    padding: 8px 10px;
    font-size: 13px;
    font-weight: normal;
}

QLineEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDateEdit:focus, QDateTimeEdit:focus {
    border: 1px solid #2563EB;
}

QLineEdit::placeholder {
    color: #94A3B8;
}

/* Tarih Kutusu Ok Butonu */
QDateEdit::drop-down, QDateTimeEdit::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;
    border-left: 1px solid #CBD5E1;
    background-color: #F1F5F9;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
QDateEdit::down-arrow, QDateTimeEdit::down-arrow {
    image: url(ui/icons/down-chevron-svgrepo-com.svg);
    width: 12px;
    height: 12px;
}

/* ===== TAKVİM PENCERESİ (POPUP) ===== */
QCalendarWidget QWidget {
    background-color: #FFFFFF;
    color: #0F172A;
}

QCalendarWidget QToolButton {
    color: #0F172A;
    background-color: #F1F5F9;
    icon-size: 20px;
    font-weight: bold;
}
QCalendarWidget QToolButton:hover {
    background-color: #F1F5F9;
    border-radius: 4px;
}

QCalendarWidget QAbstractItemView:enabled {
    background-color: #FFFFFF;
    color: #0F172A;
    selection-background-color: #2563EB;
    selection-color: #FFFFFF;
}
QCalendarWidget QAbstractItemView:disabled {
    color: #94A3B8;
}

QCalendarWidget QSpinBox {
    background-color: #FFFFFF;
    color: #0F172A;
    selection-background-color: #2563EB;
    selection-color: #FFFFFF;
}

/* ===== COMBOBOX (GENEL) ===== */
QComboBox {
    background-color: #FFFFFF;
    color: #0F172A;
    border: 1px solid #CBD5E1;
    border-radius: 10px;
    padding: 8px 10px;
    padding-right: 34px; 
    font-size: 13px;
    font-weight: normal;
}
QComboBox:hover, QComboBox:focus { border: 1px solid #2563EB; }
QComboBox::down-arrow {
    image: url(./ui/icons/down-chevron-svgrepo-com.svg);
    width: 12px;
    height: 12px;
}
QComboBox::drop-down {
    subcontrol-origin: padding; subcontrol-position: top right; width: 28px;
    border-left: 1px solid #CBD5E1; background-color: #F1F5F9; 
    border-top-right-radius: 10px; border-bottom-right-radius: 10px;
}
QComboBox::drop-down:hover { background-color: #E0E7FF; }
QComboBox QAbstractItemView {
    background-color: #FFFFFF; color: #0F172A;
    border: 1px solid #CBD5E1; selection-background-color: #DBEAFE; selection-color: #0F172A;
}

/* ===== TABLO (GENEL) ===== */
QTableWidget {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    gridline-color: #E2E8F0;
    color: #0F172A;
    font-size: 14px;
    font-weight: normal; 
    selection-background-color: #e8f0fe;
    selection-color: #1967d2;
}

QHeaderView { background-color: #F1F5F9; border: none; }

QHeaderView::section {
    background-color: #f8f9fa;
    color: #5f6368;
    font-weight: bold;
    font-size: 13px;
    padding: 8px;
    border: none;
    border-bottom: 1px solid #E2E8F0;
}

QTableWidget QHeaderView::section:vertical {
    padding-left: 4px;
}

QTableCornerButton::section { background-color: #F1F5F9; border: none; }

QTableWidget::item:selected { 
    background-color: #DBEAFE; 
    color: #0F172A; 
}

/* ===== BUTONLAR (GENEL) ===== */
QPushButton {
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600; 
}

QPushButton#primaryBtn {
    background-color: #2563EB; color: white; border: none;
}
QPushButton#primaryBtn:hover { background-color: #1D4ED8; }
QPushButton#primaryBtn:pressed { background-color: #1E3A8A; }
QPushButton#primaryBtn:disabled { background-color: #94A3B8; }

QPushButton#ghostBtn {
    background-color: #F1F5F9; color: #0F172A; border: 1px solid #E2E8F0;
}
QPushButton#ghostBtn:hover { background-color: #E2E8F0; }
QPushButton#ghostBtn:pressed { background-color: #CBD5E1; }

QPushButton#dangerBtn {
    background-color: #EF4444; color: white; border: none;
}
QPushButton#dangerBtn:hover { background-color: #DC2626; }
QPushButton#dangerBtn:pressed { background-color: #991B1B; }


/* ============================================================
   MESSAGE BOX (Siyah Ekran Düzeltmesi)
   ============================================================ */
QMessageBox {
    background-color: #FFFFFF; 
    border: 1px solid #E2E8F0; 
}
QMessageBox QLabel {
    color: #0F172A; 
    font-size: 13px; 
    font-weight: normal;
    background-color: transparent;
}
QMessageBox QPushButton {
    background-color: #F1F5F9; 
    color: #334155; 
    border: 1px solid #CBD5E1; 
    border-radius: 6px; 
    padding: 6px 16px; 
    min-width: 80px; 
    font-weight: 600;
}
QMessageBox QPushButton:hover { background-color: #E2E8F0; }
QMessageBox QPushButton:pressed { background-color: #CBD5E1; }


/* ===== MODERN DASHBOARD KARTLARI (GENEL) ===== */
QFrame#modernCard {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    border-bottom: 4px solid #cbd5e1; 
}
QFrame#modernCard:hover {
    border: 1px solid #3b82f6;
    border-bottom: 4px solid #3b82f6;
    background-color: #f8fafc;
}
QLabel#cardTitle { font-size: 14px; font-weight: bold; color: #64748b; }
QLabel#cardValue { font-size: 32px; font-weight: 800; color: #1e293b; }

/* ===== DİĞER KARTLAR ===== */
QFrame#statCard, QFrame#bookingCard, QFrame#returnCard {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
}
QFrame#returnCard QLabel {
    font-weight: normal;
    font-size: 14px;
}


/* ============================================================
   [YENİ] RENTAL PAGE İÇİN ÖZEL MODERN STİLLER
   ============================================================ */
#RentalPageWidget QLabel#pageTitle {
    font-size: 26px; font-weight: 800; color: #1e293b;
}
#RentalPageWidget QFrame#summaryCard {
    background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px;
}
#RentalPageWidget QFrame#filterFrame {
    background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px;
}
#RentalPageWidget QLineEdit, 
#RentalPageWidget QComboBox, 
#RentalPageWidget QDateEdit {
    background-color: #FFFFFF; color: #334155; border: 1px solid #E2E8F0;
    border-radius: 10px; padding: 8px 15px; font-size: 13px; font-weight: bold;
}
#RentalPageWidget QLineEdit:focus, 
#RentalPageWidget QComboBox:focus, 
#RentalPageWidget QDateEdit:focus {
    border: 2px solid #3b82f6;
}
#RentalPageWidget QComboBox::drop-down, 
#RentalPageWidget QDateEdit::drop-down {
    border: none; width: 30px;
}
#RentalPageWidget QComboBox::down-arrow, 
#RentalPageWidget QDateEdit::down-arrow {
    image: url(ui/icons/down-chevron-svgrepo-com.svg); width: 12px; height: 12px;
}
#RentalPageWidget QTableWidget {
    background-color: transparent; border: none; gridline-color: transparent; outline: none;
}
#RentalPageWidget QHeaderView::section {
    background-color: transparent; border: none; border-bottom: 2px solid #E2E8F0;
    color: #94a3b8; font-weight: bold; text-transform: uppercase; font-size: 11px;
    padding: 5px; text-align: left;
}
#RentalPageWidget QTableWidget::item {
    padding-top: 15px; padding-bottom: 15px; padding-left: 10px;
    border-bottom: 1px solid #f1f5f9; color: #334155;
}
#RentalPageWidget QTableWidget::item:selected {
    background-color: #f0f9ff; color: #0f172a; border-left: 4px solid #3b82f6;
}
#RentalPageWidget QLabel#labelGray { color: #64748b; font-size: 14px; }
#RentalPageWidget QLabel#labelDark { color: #334155; font-size: 14px; font-weight: 600; }
#RentalPageWidget QLabel#labelTotal { font-size: 26px; font-weight: 900; color: #2563EB; }
#RentalPageWidget QLabel#labelSuccess { color: #10b981; font-weight: bold; }
#RentalPageWidget QLabel#priceBadge {
    background-color: #dcfce7; color: #15803d; border-radius: 10px; 
    padding: 4px 8px; font-weight: bold; font-size: 12px;
}
#RentalPageWidget QComboBox QAbstractItemView {
    background-color: #FFFFFF; color: #334155;
    border: 1px solid #E2E8F0; selection-background-color: #EFF6FF;
    selection-color: #2563EB; outline: none; font-weight: bold;
}


/* ============================================================
   [YENİ] RETURNS PAGE İÇİN ÖZEL STİLLER (EKSİK OLAN KISIM)
   ============================================================ */

#ReturnsPageWidget QLabel#pageTitle {
    font-size: 26px; font-weight: 800; color: #1e293b;
}

/* KART TASARIMI (2px ÇERÇEVE EKLENDİ) */
#ReturnsPageWidget QFrame#summaryCard {
    background-color: #FFFFFF; 
    border: 2px solid #E2E8F0;  /* 2px Çerçeve */
    border-radius: 20px;
}
#ReturnsPageWidget QFrame#filterFrame {
    background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px;
}

/* INPUTLAR */
#ReturnsPageWidget QLineEdit, 
#ReturnsPageWidget QComboBox, 
#ReturnsPageWidget QDateEdit,
#ReturnsPageWidget QSpinBox {
    background-color: #FFFFFF; color: #334155; border: 1px solid #E2E8F0;
    border-radius: 10px; padding: 8px 15px; font-size: 13px; font-weight: bold;
}
#ReturnsPageWidget QLineEdit:focus, 
#ReturnsPageWidget QComboBox:focus, 
#ReturnsPageWidget QDateEdit:focus,
#ReturnsPageWidget QSpinBox:focus {
    border: 2px solid #3b82f6;
}

/* DROPDOWN */
#ReturnsPageWidget QComboBox::drop-down, 
#ReturnsPageWidget QDateEdit::drop-down {
    border: none; width: 30px;
}
#ReturnsPageWidget QComboBox::down-arrow, 
#ReturnsPageWidget QDateEdit::down-arrow {
    image: url(ui/icons/down-chevron-svgrepo-com.svg); width: 12px; height: 12px;
}
/* Filtre menüsünün içi kalın olsun */
#ReturnsPageWidget QComboBox QAbstractItemView {
    background-color: #FFFFFF; color: #334155;
    border: 1px solid #E2E8F0; selection-background-color: #EFF6FF;
    selection-color: #2563EB; outline: none; font-weight: bold;
}

/* TABLO */
#ReturnsPageWidget QTableWidget {
    background-color: transparent; border: none; gridline-color: transparent; outline: none;
}
#ReturnsPageWidget QHeaderView::section {
    background-color: transparent; border: none; border-bottom: 2px solid #E2E8F0;
    color: #94a3b8; font-weight: bold; text-transform: uppercase; font-size: 11px;
    padding: 5px; text-align: left;
}
#ReturnsPageWidget QTableWidget::item {
    padding-top: 15px; padding-bottom: 15px; padding-left: 10px;
    border-bottom: 1px solid #f1f5f9; color: #334155;
}
#ReturnsPageWidget QTableWidget::item:selected {
    background-color: #f0f9ff; color: #0f172a; border-left: 4px solid #3b82f6;
}

/* ETİKETLER (RENK DÜZELTMELERİ BURADA) */
#ReturnsPageWidget QLabel#labelGray { color: #64748b; font-size: 14px; }
#ReturnsPageWidget QLabel#labelDark { color: #334155; font-size: 14px; font-weight: 600; }

/* TOTAL PAY RENGİ (MAVİ) */
#ReturnsPageWidget QLabel#labelTotal { 
    font-size: 26px; 
    font-weight: 900; 
    color: #2563EB; /* MAVİ */ 
}

#ReturnsPageWidget QLabel#labelDanger { font-size: 14px; font-weight: bold; color: #EF4444; }

/* BUTON */
#ReturnsPageWidget QPushButton#primaryBtn {
    background-color: #2563EB; color: white; border: none; border-radius: 12px; font-weight: bold;
}
#ReturnsPageWidget QPushButton#primaryBtn:hover { background-color: #1d4ed8; }
#ReturnsPageWidget QPushButton#primaryBtn:disabled { background-color: #e2e8f0; color: #94a3b8; }
"""

# ============================================================
# 2. ŞİFRE DEĞİŞTİRME PENCERESİ STİLİ
# ============================================================
PASSWORD_DIALOG_STYLE = """
    QDialog {
        background-color: #FFFFFF;
        color: #0F172A;
    }
    QLabel {
        color: #334155;
        font-weight: bold;
        font-size: 12px;
        margin-bottom: 5px;
    }
    QLineEdit {
        background-color: #F8FAFC;
        border: 1px solid #CBD5E1;
        padding: 10px;
        color: #0F172A;
        border-radius: 6px;
        font-size: 14px;
        margin-bottom: 15px;
    }
    QLineEdit:focus {
        border: 1px solid #5865F2;
        background-color: #FFFFFF;
    }
    QPushButton {
        padding: 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 14px;
    }
    QPushButton#cancelBtn {
        background-color: transparent;
        color: #64748B;
        border: none;
    }
    QPushButton#cancelBtn:hover {
        color: #0F172A;
        text-decoration: underline;
    }
    QPushButton#saveBtn {
        background-color: #5865F2;
        color: white;
    }
    QPushButton#saveBtn:hover {
        background-color: #4752c4;
    }
    QLabel#dialogTitle {
        font-size: 20px; 
        color: #0F172A;
        margin-bottom: 10px;
    }
    QLabel#dialogDesc {
        font-weight: normal; 
        color: #64748B;
        margin-bottom: 20px;
    }
"""
