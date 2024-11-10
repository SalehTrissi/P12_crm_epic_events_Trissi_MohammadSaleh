from .database import engine, Base
from EpicEventsCRM.models.employee_model import Employee  # noqa
from EpicEventsCRM.models.event_model import Event  # noqa
from EpicEventsCRM.models.client_model import Client  # noqa
from EpicEventsCRM.models.contract_model import Contract  # noqa


def create_tables():
    # Create all tables in the database based on models
    Base.metadata.create_all(engine)
    print("All tables created successfully.")


if __name__ == "__main__":
    create_tables()
