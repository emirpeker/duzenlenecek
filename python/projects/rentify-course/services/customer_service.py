# services/customer_service.py

from database.db_connection import get_connection


def get_all_customers():
    conn = get_connection()
    if not conn:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT
                c.id,
                c.first_name,
                c.last_name,
                c.national_id,
                u.username,
                u.email
            FROM customers c
            JOIN users u ON c.user_id = u.id
            ORDER BY c.id
            """
        )
        return cursor.fetchall()

    except Exception as e:
        print("Error fetching customers:", e)
        return []

    finally:
        conn.close()


def get_customer_id_by_user_id(user_id: int) -> int | None:
    conn = get_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id FROM customers WHERE user_id = %s",
            (user_id,),
        )
        row = cursor.fetchone()
        return row["id"] if row else None

    except Exception as e:
        print("Error fetching customer by user_id:", e)
        return None

    finally:
        conn.close()
