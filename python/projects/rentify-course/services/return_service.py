# services/return_service.py

from database.db_connection import get_connection
from datetime import date


def calculate_late_fee(planned_end_date, return_date, daily_price):
    """
    Geciken her gün için günlük ücretin 2 katı ceza
    """
    if not planned_end_date or return_date <= planned_end_date:
        return 0.0

    overdue_days = (return_date - planned_end_date).days
    return overdue_days * float(daily_price) * 2


def process_detailed_return(
    rental_id: int,
    car_id: int,
    return_date: date,
    end_km: int,
    notes: str = "",
    damage_fee: float = 0.0,
):
    conn = get_connection()
    if not conn:
        return False, "Database connection failed."

    try:
        cursor = conn.cursor(dictionary=True)

        # Kiralamayı al
        cursor.execute(
            """
            SELECT
                r.planned_end_date,
                r.start_odometer,
                c.daily_price
            FROM rentals r
            JOIN cars c ON r.car_id = c.id
            WHERE r.id = %s
            """,
            (rental_id,),
        )
        rental = cursor.fetchone()

        if not rental:
            return False, "Rental not found."

        penalty_fee = calculate_late_fee(
            rental["planned_end_date"], return_date, rental["daily_price"]
        )

        # Kiralamayı kapat
        cursor.execute(
            """
            UPDATE rentals
            SET actual_return_date = %s
            WHERE id = %s
            """,
            (return_date, rental_id),
        )

        # Return kaydı oluştur
        cursor.execute(
            """
            INSERT INTO returns
            (
              rental_id,
              return_date,
              return_odometer,
              penalty_fee,
              damage_fee
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                rental_id,
                return_date,
                end_km,
                penalty_fee,
                damage_fee,
            ),
        )

        # Araç güncelle
        cursor.execute(
            """
            UPDATE cars
            SET status = 'available',
                kilometer = %s
            WHERE id = %s
            """,
            (end_km, car_id),
        )

        conn.commit()
        return True, "Car returned successfully."

    except Exception as e:
        conn.rollback()
        return False, f"Database Error: {str(e)}"

    finally:
        cursor.close()
        conn.close()


from datetime import date
from database.db_connection import get_connection


def quick_return_by_car_id(car_id: int):
    conn = get_connection()
    if not conn:
        return False, "Database connection error"

    try:
        cursor = conn.cursor(dictionary=True)

        # Aktif kiralamayı bul
        cursor.execute(
            """
            SELECT id
            FROM rentals
            WHERE car_id = %s AND actual_return_date IS NULL
            """,
            (car_id,),
        )
        rental = cursor.fetchone()

        if not rental:
            return False, "Active rental not found for this car"

        # Kiralamayı kapat
        cursor.execute(
            """
            UPDATE rentals
            SET actual_return_date = %s
            WHERE id = %s
            """,
            (date.today(), rental["id"]),
        )

        # Aracı müsait yap
        cursor.execute(
            "UPDATE cars SET status = 'available' WHERE id = %s",
            (car_id,),
        )

        conn.commit()
        return True, "Car returned successfully"

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()
