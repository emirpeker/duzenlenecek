from dataclasses import dataclass
from typing import Optional
import mysql.connector
from database.db_connection import get_connection
from services.password_utils import hash_password, check_password
from models import user


# ---------------------------------------------------
# SERVICE
# ---------------------------------------------------
def get_user_by_identifier(identifier: str) -> Optional[user.User]:
    conn = get_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                u.id,
                u.username,
                u.password_hash,
                u.email,
                u.role,
                c.first_name,
                c.last_name
            FROM users u 
            LEFT JOIN customers c ON u.id = c.user_id 
            WHERE u.username = %s OR u.email=%s
        """

        cursor.execute(
            query,
            (
                identifier,
                identifier,
            ),
        )
        row = cursor.fetchone()

        if row:
            return user.User(
                id=row["id"],
                username=row["username"],
                password=row["password_hash"],
                email=row["email"] or "",
                name=row["first_name"] or "",
                lastname=row["last_name"] or "",
                role=row["role"],
            )

        return None

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


def update_user_contact_info(username: str, new_email: str, new_password: str) -> bool:
    conn = get_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        if new_password:
            hashed_pw = hash_password(new_password)
            query = (
                "UPDATE users SET email = %s, password_hash = %s WHERE username = %s"
            )
            params = (new_email, hashed_pw, username)

        else:
            query = "UPDATE users SET email = %s WHERE username = %s"
            params = (new_email, username)
        cursor.execute(query, params)
        conn.commit()
        return True

    except mysql.connector.Error as err:
        print(f"Update Error: {err}")
        return False
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


def change_password(username: str, old_pass: str, new_pass: str):
    conn = get_connection()
    if conn is None:
        return False, "DB connection failed."

    try:
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT password_hash FROM users WHERE username=%s", (username,))
        row = cur.fetchone()
        if not row:
            return False, "User not found."

        # eski şifre doğru mu?
        if not check_password(old_pass, row["password_hash"]):
            return False, "Current password is incorrect."

        # yeni hash
        new_hash = hash_password(new_pass)

        cur.execute(
            "UPDATE users SET password_hash=%s WHERE username=%s", (new_hash, username)
        )
        conn.commit()

        return True, "Password updated successfully."

    except Exception as e:
        return False, f"Error: {e}"

    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass
