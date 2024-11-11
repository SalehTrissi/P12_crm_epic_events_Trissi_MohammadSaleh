from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Index,
    func,
)
from sqlalchemy.orm import relationship
from db.database import Base


class Client(Base):
    """Represents a client in the system."""

    __tablename__ = "clients"
    __table_args__ = (
        Index("idx_client_email", "email"),
        Index("idx_client_full_name", "full_name"),
    )

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    company_name = Column(String(100), nullable=True)
    creation_date = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    last_contact_date = Column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=func.now(),
    )
    sales_contact_id = Column(
        Integer, ForeignKey("employees.id"))

    # Relationships
    sales_contact = relationship(
        "Employee", back_populates="clients")
    contracts = relationship(
        "Contract", back_populates="client")

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.full_name})>"

    @property
    def contact_info(self) -> dict:
        """Returns a dictionary containing the client's contact information."""
        return {"full_name": self.full_name, "email": self.email, "phone": self.phone}
