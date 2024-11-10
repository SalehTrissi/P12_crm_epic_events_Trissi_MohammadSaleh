from sqlalchemy import Column, Integer, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    sales_contact_id = Column(Integer, ForeignKey("employees.id"))
    total_amount = Column(Float, nullable=False)
    amount_due = Column(Float, nullable=False)
    creation_date = Column(Date, nullable=False, server_default=func.now())
    is_signed = Column(Boolean, default=False)

    # Relationships
    client = relationship("Client", back_populates="contracts")
    sales_contact = relationship("Employee", back_populates="contracts")
    events = relationship("Event", back_populates="contract")

    def __repr__(self):
        return f"<Contract(id={self.id}, client_id={self.client_id})>"
