import re
from database.db_connection import get_connection
from services.password_utils import hash_password, check_password
import mysql.connector


def register_user(
    username: str,
    email: str,
    password: str,
    first_name: str,
    last_name: str,
    national_id: str,
) -> bool:

    conn = get_connection()
    if conn is None:
        return False

    cursor = None

    try:
        cursor = conn.cursor()

        #  users tablosuna ekle
        cursor.execute(
            """
            INSERT INTO users (username, email, password_hash)
            VALUES (%s, %s, %s)
            """,
            (username, email, hash_password(password)),
        )

        # eklenen user'ın id'si
        user_id = cursor.lastrowid

        #  customers tablosuna ekle
        cursor.execute(
            """
            INSERT INTO customers (user_id, first_name, last_name, national_id)
            VALUES (%s, %s, %s, %s)
            """,
            (user_id, first_name, last_name, national_id),
        )

        #  her şey OK → commit
        conn.commit()
        return True

    except mysql.connector.IntegrityError as e:
        conn.rollback()  # çok önemli
        print("Integrity Error:", e)
        return False

    except mysql.connector.Error as e:
        conn.rollback()
        print("MYSQL ERROR:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def authenticate_user(identifier: str, password: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password_hash 
        FROM users 
        WHERE username = %s OR email = %s
        """,
        (identifier, identifier),
    )

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        return False

    return check_password(password, row[0])


def is_valid_email(email: str) -> bool:
    # Basit ve etkili bir email regex deseni
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_national_id(id: str) -> bool:
    if not id.isdigit() or len(id) != 11:
        return False

    if id[0] == "0":
        return False

    digits = list(map(int, id))

    odd_sum = sum(digits[0:9:2])
    even_sum = sum(digits[1:8:2])

    tenth_digit = ((odd_sum * 7) - even_sum) % 10
    if tenth_digit != digits[9]:
        return False
    eleventh_digit = sum(digits[:10]) % 10

    if eleventh_digit != digits[10]:
        return False

    return True
