from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    support_contact_id = Column(Integer, ForeignKey("employees.id"))
    location = Column(String, nullable=True)
    attendees = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)

    # Relationships
    contract = relationship("Contract", back_populates="events")
    support_contact = relationship("Employee", back_populates="events")
    client = relationship("Client")

    def __repr__(self):
        return f"<Event(id={self.id}, contract_id={self.contract_id}, client_id={self.client_id})>"
