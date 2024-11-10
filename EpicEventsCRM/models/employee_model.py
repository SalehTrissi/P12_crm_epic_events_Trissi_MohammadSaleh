from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
import enum


class DepartmentType(enum.Enum):
    COMMERCIAL = "Commercial"
    SUPPORT = "Support"
    MANAGEMENT = "Management"


class RoleType(enum.Enum):
    SALES = "Sales"
    SUPPORT_STAFF = "Support"
    MANAGER = "Manager"


class EmployeeStatus(enum.Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    creation_date = Column(Date, nullable=False, server_default=func.now())
    role = Column(Enum(RoleType), nullable=False)
    department = Column(Enum(DepartmentType), nullable=False)
    status = Column(Enum(EmployeeStatus), nullable=False,
                    default=EmployeeStatus.ACTIVE)

    # Relationships
    clients = relationship("Client", back_populates="sales_contact")
    contracts = relationship("Contract", back_populates="sales_contact")
    events = relationship("Event", back_populates="support_contact")

    def __repr__(self):
        return (f"<Employee(id={self.id}, name={self.first_name} {self.last_name}, "
                f"department={self.department}, role={self.role})>")
