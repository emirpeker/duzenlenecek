# services/car_service.py

from database.db_connection import get_connection
from models.car import Car


def _get_or_create_model_id(brand_name: str, model_name: str) -> int:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    # Brand
    cur.execute("SELECT id FROM brands WHERE name = %s", (brand_name,))
    brand = cur.fetchone()

    if not brand:
        cur.execute("INSERT INTO brands (name) VALUES (%s)", (brand_name,))
        brand_id = cur.lastrowid
    else:
        brand_id = brand["id"]

    # Model
    cur.execute(
        "SELECT id FROM models WHERE brand_id = %s AND name = %s",
        (brand_id, model_name),
    )
    model = cur.fetchone()

    if not model:
        cur.execute(
            "INSERT INTO models (brand_id, name) VALUES (%s, %s)",
            (brand_id, model_name),
        )
        model_id = cur.lastrowid
    else:
        model_id = model["id"]

    conn.commit()
    cur.close()
    conn.close()

    return model_id


# -------------------- CRUD --------------------


def add_car(car: Car):
    model_id = _get_or_create_model_id(car.brand, car.model)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO cars (plate_number, model_id, daily_price, status, kilometer)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            car.plate_number,
            model_id,
            car.daily_price,
            car.status,
            getattr(car, "kilometer", 0),
        ),
    )

    conn.commit()
    cur.close()
    conn.close()


def get_all_cars():
    conn = get_connection()
    if conn is None:
        return []

    try:
        cur = conn.cursor(dictionary=True)

        # Normalize edilmiş veritabanı sorgusu
        cur.execute(
            """
            SELECT
                c.id,
                c.plate_number,
                b.name AS brand,
                m.name AS model,
                c.daily_price,
                c.status,
                c.kilometer
            FROM cars c
            JOIN models m ON c.model_id = m.id
            JOIN brands b ON m.brand_id = b.id
            ORDER BY c.id
            """
        )

        rows = cur.fetchall()
        return [Car(**row) for row in rows]

    except Exception as e:
        print(f"Error fetching cars: {e}")
        return []

    finally:
        if conn:
            cur.close()
            conn.close()


def get_available_cars():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT
            c.id,
            c.plate_number,
            b.name AS brand,
            m.name AS model,
            c.daily_price,
            c.status,
            c.kilometer
        FROM cars c
        JOIN models m ON c.model_id = m.id
        JOIN brands b ON m.brand_id = b.id
        WHERE c.status = 'available'
        """
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [Car(**row) for row in rows]


def update_car(car: Car):
    model_id = _get_or_create_model_id(car.brand, car.model)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE cars
        SET
            plate_number = %s,
            model_id = %s,
            daily_price = %s,
            status = %s,
            kilometer = %s
        WHERE id = %s
        """,
        (
            car.plate_number,
            model_id,
            car.daily_price,
            car.status,
            getattr(car, "kilometer", 0),
            car.id,
        ),
    )

    conn.commit()
    cur.close()
    conn.close()


def delete_car(car_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM cars WHERE id = %s", (car_id,))
    conn.commit()

    cur.close()
    conn.close()
