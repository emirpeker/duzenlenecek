from database.db_connection import get_connection
from datetime import date, timedelta, datetime
from services.customer_service import get_customer_id_by_user_id


def get_user_rental_count(user_id):
    """
    Kullanıcının sadakat seviyesini (Bronze, Silver, Gold) hesaplamak için
    geçmiş kiralama sayısını veritabanından çeker.
    """
    conn = get_connection()
    if conn is None:
        return 0
    try:
        cursor = conn.cursor()
        cust_id = get_customer_id_by_user_id(user_id)
        if not cust_id:
            return 0

        # Bu müşterinin kaç tane kaydı var say
        cursor.execute(
            "SELECT COUNT(*) FROM rentals WHERE customer_id = %s", (cust_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else 0
    except:
        return 0
    finally:
        if conn:
            conn.close()


def get_user_discount_rate(user_id):
    count = get_user_rental_count(user_id)

    if count >= 30:
        return 0.15, "Diamond"
    elif count >= 15:
        return 0.10, "Gold"
    elif count >= 5:
        return 0.05, "Silver"
    else:
        return 0.0, "Standard"


def rent_car(car_id: int, user_id: int, days: int, start_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # 1. Arabayı Kilitle (Aynı anda başkası kiralayamasın diye)
        cursor.execute(
            "SELECT status, daily_price, kilometer FROM cars WHERE id=%s FOR UPDATE",
            (car_id,),
        )
        row = cursor.fetchone()

        if not row or row[0] != "available":
            return False, "Car is not available"  # Araç müsait değil

        customer_id = get_customer_id_by_user_id(user_id)
        if not customer_id:
            return False, "Customer profile not found"

        daily_price = float(row[1])
        current_km = row[2] if row[2] else 0

        # --- İNDİRİM HESAPLAMA MANTIĞI ---
        rental_count = get_user_rental_count(user_id)
        discount_rate = 0.0
        tier_name = "Standard"

        # Seviyeleri belirle
        if rental_count >= 30:
            discount_rate = 0.15  # Platinum Üye: %15 İndirim
            tier_name = "Diamond"
        elif rental_count >= 15:
            discount_rate = 0.10  # Gold Üye: %10 İndirim
            tier_name = "Gold"
        elif rental_count >= 5:
            discount_rate = 0.05  # Silver Üye: %5 İndirim
            tier_name = "Silver"

        # Fiyatı Hesapla
        base_total_price = daily_price * days
        discount_amount = base_total_price * discount_rate
        final_total_price = base_total_price - discount_amount
        # ----------------------------------

        # Tarih Ayarlaması
        if start_date:
            if isinstance(start_date, str):
                start = datetime.strptime(start_date, "%Y-%m-%d").date()
            else:
                start = start_date
        else:
            start = date.today()

        end = start + timedelta(days=days)

        # 2. Kiralama Kaydını Oluştur (INSERT)
        # Not: Tabloda 'end_date' yerine 'planned_end_date' var, onu kullandım.
        cursor.execute(
            """
            INSERT INTO rentals
            (car_id, customer_id, start_date, planned_end_date, total_price, start_odometer)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (car_id, customer_id, start, end, final_total_price, current_km),
        )

        # 3. Araba durumunu güncelle (available -> rented)
        cursor.execute("UPDATE cars SET status='rented' WHERE id=%s", (car_id,))

        conn.commit()

        # Başarı mesajı (İndirimi kullanıcıya gösterelim)
        if discount_rate > 0:
            msg = f"Success! {tier_name} Discount (-{int(discount_amount)} TL) applied."
        else:
            msg = "Car rented successfully."

        return True, msg

    except Exception as e:
        conn.rollback()
        print(f"Rent Error: {e}")
        return False, str(e)

    finally:
        cursor.close()
        conn.close()


def get_active_rentals(current_user_id, role):
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        # NORMALİZASYON GÜNCELLEMESİ:
        # Arabanın markasını ve modelini almak için 3 tabloyu birleştiriyoruz (JOIN).
        # cars -> models -> brands
        base_query = """
            SELECT 
                r.id as rental_id,
                r.car_id,
                c.plate_number,
                b.name as brand,
                m.name as model,
                c.daily_price,
                c.kilometer as current_car_km, 
                r.start_odometer, 
                u.username,
                r.start_date,
                r.planned_end_date as end_date,
                r.total_price  
            FROM rentals r
            JOIN cars c ON r.car_id = c.id
            JOIN models m ON c.model_id = m.id
            JOIN brands b ON m.brand_id = b.id
            JOIN customers cust ON r.customer_id = cust.id
            JOIN users u ON cust.user_id = u.id
            WHERE r.actual_return_date IS NULL
        """
        # Not: Aktif kiralama demek, 'actual_return_date' (gerçek iade tarihi) henüz boş (NULL) demektir.

        params = ()
        if role == "user":
            base_query += " AND u.id = %s"
            params = (current_user_id,)

        cursor.execute(base_query, params)
        return cursor.fetchall()

    except Exception as e:
        print(f"Error fetching active rentals: {e}")
        return []
    finally:
        if conn:
            conn.close()


def get_all_rentals():
    """Tüm kiralama geçmişini çeker (Dashboard ve Admin panel için)"""
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        # Burada da JOIN kullanarak isimleri alıyoruz
        query = """
            SELECT 
                r.id, 
                r.car_id,
                r.start_date, 
                r.planned_end_date as end_date,
                r.actual_return_date,
                r.total_price, 
                c.plate_number, 
                b.name as brand, 
                m.name as model,
                u.username,
                u.id as user_id 
            FROM rentals r
            LEFT JOIN cars c ON r.car_id = c.id
            LEFT JOIN models m ON c.model_id = m.id
            LEFT JOIN brands b ON m.brand_id = b.id
            LEFT JOIN customers cust ON r.customer_id = cust.id
            LEFT JOIN users u ON cust.user_id = u.id
            ORDER BY r.start_date DESC
        """
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print(f"Error fetching all rentals: {e}")
        return []
    finally:
        if conn:
            conn.close()


def return_car(
    rental_id, return_date, return_odometer, late_days, penalty_fee, damage_fee
):
    conn = get_connection()
    if conn is None:
        return False, "Database connection failed"

    try:
        cursor = conn.cursor()

        # 1. Rentals tablosunu güncelle (İade tarihi işle)
        # Not: actual_return_date sütununu dolduruyoruz
        cursor.execute(
            "UPDATE rentals SET actual_return_date = %s WHERE id = %s",
            (return_date, rental_id),
        )

        # 2. Returns tablosuna kayıt at (Detaylar)
        cursor.execute(
            """
            INSERT INTO returns 
            (rental_id, return_date, return_odometer, late_days, penalty_fee, damage_fee)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                rental_id,
                return_date,
                return_odometer,
                late_days,
                penalty_fee,
                damage_fee,
            ),
        )

        # 3. Arabayı tekrar 'available' (müsait) yap ve kilometresini güncelle
        # Önce rental'dan car_id'yi bulalım
        cursor.execute("SELECT car_id FROM rentals WHERE id = %s", (rental_id,))
        car_row = cursor.fetchone()

        if car_row:
            car_id = car_row[0]
            cursor.execute(
                "UPDATE cars SET status='available', kilometer=%s WHERE id=%s",
                (return_odometer, car_id),
            )

        conn.commit()
        return True, "Car returned successfully!"

    except Exception as e:
        conn.rollback()
        print(f"Return Error: {e}")
        return False, str(e)
    finally:
        if conn:
            conn.close()
