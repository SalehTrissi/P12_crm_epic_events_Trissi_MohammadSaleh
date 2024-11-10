from sqlalchemy import inspect
from db.database import engine


def test_tables_exist():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    expected_tables = {"employees", "events", "clients", "contracts"}
    missing_tables = expected_tables - set(tables)

    if missing_tables:
        print(f"Missing tables: {', '.join(missing_tables)}")
        return False

    print("All tables are present in the database.")
    return True


if __name__ == "__main__":
    if test_tables_exist():
        print("Table creation test passed.")
    else:
        print("Table creation test failed.")
