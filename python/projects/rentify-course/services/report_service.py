# services/report_service.py

from database.db_connection import get_connection


# =================================================
# SUMMARY REPORT
# =================================================
def get_summary_report() -> dict:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
              (SELECT COUNT(*) FROM cars) AS total_cars,
              (SELECT COUNT(*) FROM cars WHERE status = 'rented') AS rented_cars,
              (SELECT COUNT(*) FROM rentals) AS total_rentals,
              (SELECT IFNULL(SUM(total_price), 0) FROM rentals) AS total_income
            """
        )
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


# =================================================
# RECENT RENTALS
# =================================================
def get_recent_rentals(limit: int = 50) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
            r.id AS rental_id,
            r.customer_id,
            u.id AS user_id,
            u.username,
            b.name AS brand,
            m.name AS model,
            r.start_date,
            r.planned_end_date,
            r.actual_return_date,
            CASE
              WHEN r.actual_return_date IS NULL THEN 'ACTIVE'
              ELSE 'RETURNED'
            END AS status,
            r.total_price
          FROM rentals r
          JOIN customers cu ON r.customer_id = cu.id
          JOIN users u ON cu.user_id = u.id
          JOIN cars c ON r.car_id = c.id
          JOIN models m ON c.model_id = m.id
          JOIN brands b ON m.brand_id = b.id
          ORDER BY r.start_date DESC
          LIMIT %s
            """,
            (limit,),
        )
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


# =================================================
# OVERDUE RENTALS
# =================================================
def get_overdue_rentals() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
              b.name AS brand,
              m.name AS model,
              cu.first_name,
              cu.last_name,
              r.start_date,
              r.planned_end_date,
              r.actual_return_date,
              DATEDIFF(CURDATE(), r.planned_end_date) AS days,
              r.total_price
            FROM rentals r
            JOIN cars c ON r.car_id = c.id
            JOIN models m ON c.model_id = m.id
            JOIN brands b ON m.brand_id = b.id
            JOIN customers cu ON r.customer_id = cu.id
            WHERE r.actual_return_date IS NULL
              AND r.planned_end_date < CURDATE()
            ORDER BY r.planned_end_date ASC
            """
        )
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


# =================================================
# MONTHLY REVENUE
# =================================================
def get_monthly_revenue() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
              DATE_FORMAT(start_date, '%Y-%m') AS month,
              SUM(total_price) AS revenue
            FROM rentals
            GROUP BY month
            ORDER BY month DESC
            """
        )
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()
