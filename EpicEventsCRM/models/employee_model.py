from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum as SqlEnum,
    DateTime,
    func,
    Index,
)
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher, exceptions as argon2_exceptions
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
    """Represents an employee in the organization."""

    __tablename__ = "employees"
    __table_args__ = (Index('idx_employee_email', 'email'),)

    id = Column(Integer, primary_key=True, index=True)
    employee_number = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    role = Column(SqlEnum(RoleType), nullable=False)
    department = Column(SqlEnum(DepartmentType), nullable=False)
    status = Column(
        SqlEnum(EmployeeStatus),
        nullable=False,
        default=EmployeeStatus.ACTIVE.value,
    )

    # Relationships
    clients = relationship(
        "Client", back_populates="sales_contact", lazy="dynamic")
    contracts = relationship(
        "Contract", back_populates="sales_contact", lazy="dynamic")
    events = relationship(
        "Event", back_populates="support_contact", lazy="dynamic")

    password_hasher = PasswordHasher()

    def __repr__(self):
        return (
            f"<Employee(id={self.id}, name={
                self.first_name} {self.last_name}, "
            f"department={self.department.value}, role={self.role.value})>"
        )

    @property
    def full_name(self):
        """Returns the full name of the employee."""

        return f"{self.first_name} {self.last_name}"

    def set_password(self, password):
        """Hashes and sets the user's password."""

        self.hashed_password = self.password_hasher.hash(password)

    def verify_password(self, password):
        """Verifies the user's password."""
        try:
            return self.password_hasher.verify(self.hashed_password, password)
        except argon2_exceptions.VerifyMismatchError:
            return False
        except argon2_exceptions.VerificationError:
            return False
        except Exception:
            # Optionally log the exception details here
            return False

    def get_permissions(self):
        """Assigns permissions based on role and department."""

        permissions = []
        if self.department == DepartmentType.COMMERCIAL:
            permissions.extend(
                ["view_clients", "create_client", "update_client"])
            if self.role == RoleType.SALES:
                permissions.append("manage_contracts")
        elif self.department == DepartmentType.MANAGEMENT:
            permissions.extend(["manage_all_contracts", "assign_support"])
        elif self.department == DepartmentType.SUPPORT:
            permissions.extend(["view_events", "update_event"])

        return permissions
