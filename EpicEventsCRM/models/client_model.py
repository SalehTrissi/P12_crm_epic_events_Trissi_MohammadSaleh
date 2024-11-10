from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    creation_date = Column(Date, nullable=False, server_default=func.now())
    last_contact_date = Column(
        Date, nullable=True, onupdate=func.current_timestamp())
    sales_contact_id = Column(Integer, ForeignKey("employees.id"))

    # Relationships
    sales_contact = relationship("Employee", back_populates="clients")
    contracts = relationship("Contract", back_populates="client")

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.full_name})>"
