from db.database import SessionLocal
from sqlalchemy.exc import OperationalError
from sqlalchemy import text


def test_database_connection():
    try:
        # Try to connect to the database
        session = SessionLocal()

        # Simple test to check connection
        session.execute(text("SELECT 1"))
        print("Database connection successful!")

    except OperationalError as e:
        print("Database connection failed:", e)

    finally:
        session.close()


if __name__ == "__main__":
    test_database_connection()
