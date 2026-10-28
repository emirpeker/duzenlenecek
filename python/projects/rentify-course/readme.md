# 🚗 Rentify – Araç Kiralama Yönetim Sistemi

**Rentify**, Python ve PyQt6 kullanılarak geliştirilmiş, MySQL (MariaDB) tabanlı bir **masaüstü araç kiralama otomasyon sistemidir**.  
Sistem; **admin** ve **kullanıcı** rollerine göre ayrılmış ekranlar, kiralama–iade süreçleri ve detaylı raporlama özellikleri sunar.

---

## ✨ Özellikler

### 👤 Kimlik Doğrulama

- Kullanıcı kayıt & giriş sistemi
- Şifrelerin **bcrypt** ile hashlenmesi
- Rol bazlı yetkilendirme (Admin / User)

### 🚘 Araç Yönetimi

- Araç listeleme
- Araç durumu takibi (Available / Rented)
- Marka & model ilişkili yapı

### 📄 Kiralama & İade

- Araç kiralama
- Aktif kiralamaları görüntüleme
- İade işlemleri
- Gecikme süresine göre ceza hesaplama

### 📊 Raporlama

- Özet raporlar
- Son kiralamalar
- Kullanıcıya özel rapor ekranı
- Admin & User için ayrı rapor sayfaları

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **PyQt6**
- **MySQL / MariaDB**
- **bcrypt**
- **Qt Designer**
- **XAMPP**

---

## 🗄️ Veritabanı

- Veritabanı adı: **`rentacarr`**
- SQL dosyası: **`rentacarr.sql`**
- MySQL / MariaDB uyumludur
- Foreign Key ilişkileri kullanılmıştır

### Temel Tablolar

- `users`
- `customers`
- `cars`
- `rentals`
- `returns`
- `brands`
- `models`

---

## 📂 Proje Yapısı

```text
Rentify/
│
├── main.py
│
├── database/
│   └── db_connection.py
│
├── models/
│   ├── user.py
│   ├── customer.py
│   ├── car.py
│   ├── rental.py
│   └── return.py
│
├── pages/
│   ├── login_page.py
│   ├── signup_page.py
│   ├── main_window.py
│   ├── dashboard_page.py
│   ├── car_page.py
│   ├── rental_page.py
│   ├── return_page.py
│   ├── profile_page.py
│   ├── reports_page.py
│   └── user_reports_page.py
│
├── services/
│   ├── auth_service.py
│   ├── user_service.py
│   ├── customer_service.py
│   ├── car_service.py
│   ├── rental_service.py
│   ├── return_service.py
│   ├── report_service.py
│   └── password_utils.py
│
├── ui/
│   ├── login.ui
│   ├── signup.ui
│   ├── icons/
│   └── stylesheet.py
│
├── rentacarr.sql
├── .gitignore
└── README.md
```

# 🚗 Rentify – Car Rental Management System

**Rentify** is a desktop-based **Car Rental Management System** developed using **Python**, **PyQt6**, and **MySQL (MariaDB)**.  
The system provides role-based access (**Admin / User**) and manages the entire car rental process from rental to return, including reporting.

---

## ✨ Features

### 👤 Authentication & Users

- User registration & login
- Secure password hashing using **bcrypt**
- Role-based authorization (Admin / User)

### 🚘 Car Management

- Car listing and management
- Car status tracking (Available / Rented)
- Brand & model relationship structure

### 📄 Rental & Return

- Car rental operations
- Active rental tracking
- Return process
- Late fee calculation

### 📊 Reporting

- Summary reports
- Recent rentals
- User-specific reports
- Separate report pages for Admin and User roles

---

## 🛠️ Technologies Used

- **Python 3**
- **PyQt6**
- **MySQL / MariaDB**
- **bcrypt**
- **Qt Designer**
- **XAMPP**

---

## 🗄️ Database

- Database name: **`rentacarr`**
- SQL file: **`rentacarr.sql`**
- Compatible with MySQL / MariaDB
- Foreign key relationships are used

### Main Tables

- `users`
- `customers`
- `cars`
- `rentals`
- `returns`
- `brands`
- `models`

---

## 📂 Project Structure

```text
Rentify/
│
├── main.py
│
├── database/
│   └── db_connection.py
│
├── models/
│   ├── user.py
│   ├── customer.py
│   ├── car.py
│   ├── rental.py
│   └── return.py
│
├── pages/
│   ├── login_page.py
│   ├── signup_page.py
│   ├── main_window.py
│   ├── dashboard_page.py
│   ├── car_page.py
│   ├── rental_page.py
│   ├── return_page.py
│   ├── profile_page.py
│   ├── reports_page.py
│   └── user_reports_page.py
│
├── services/
│   ├── auth_service.py
│   ├── user_service.py
│   ├── customer_service.py
│   ├── car_service.py
│   ├── rental_service.py
│   ├── return_service.py
│   ├── report_service.py
│   └── password_utils.py
│
├── ui/
│   ├── login.ui
│   ├── signup.ui
│   ├── icons/
│   └── stylesheet.py
│
├── rentacarr.sql
├── .gitignore
└── README.md
```
