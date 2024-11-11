from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    Boolean,
    Index,
    func,
)
from sqlalchemy.orm import relationship
from db.database import Base


class Contract(Base):
    """Represents a contract between a client and the company."""

    __tablename__ = "contracts"
    __table_args__ = (
        Index("idx_contract_client_id", "client_id"),
        Index("idx_contract_sales_contact_id", "sales_contact_id"),
    )

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    sales_contact_id = Column(
        Integer, ForeignKey("employees.id"))
    total_amount = Column(Float, nullable=False)
    amount_due = Column(Float, nullable=False)
    creation_date = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    is_signed = Column(Boolean, default=False, nullable=False)

    # Relationships
    client = relationship("Client", back_populates="contracts")
    sales_contact = relationship(
        "Employee", back_populates="contracts")
    events = relationship("Event", back_populates="contract")

    def __repr__(self):
        return f"<Contract(id={self.id}, client_id={self.client_id})>"

    @property
    def is_fully_paid(self):
        """Checks if the contract is fully paid."""

        return self.amount_due <= 0.0
