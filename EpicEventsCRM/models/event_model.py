from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import relationship
from db.database import Base


class Event(Base):
    """Represents an event scheduled under a contract."""

    __tablename__ = "events"
    __table_args__ = (
        Index("idx_event_contract_id", "contract_id"),
        Index("idx_event_client_id", "client_id"),
        Index("idx_event_support_contact_id", "support_contact_id"),
    )

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    support_contact_id = Column(
        Integer, ForeignKey("employees.id"))
    location = Column(String(255), nullable=True)
    attendees = Column(Integer, nullable=True)
    notes = Column(String(1000), nullable=True)

    # Relationships
    contract = relationship(
        "Contract", back_populates="events")
    support_contact = relationship(
        "Employee", back_populates="events")
    client = relationship("Client", back_populates="events")

    def __repr__(self):
        return (
            f"<Event(id={self.id}, contract_id={self.contract_id}, "
            f"client_id={self.client_id})>"
        )

    @property
    def duration(self):
        """Calculates the duration of the event in hours."""

        duration_timedelta = self.end_date - self.start_date
        return duration_timedelta.total_seconds() / 3600.0
