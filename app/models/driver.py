from datetime import datetime

from sqlalchemy import INTEGER, Column, DateTime, String

from app.common.database import DBBaseCustom


class DriverModel(DBBaseCustom):
    __tablename__ = "driver"
    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(255), nullable=True)
    surname = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    gender = Column(String(30), nullable=True)
    birth_day = Column(DateTime, nullable=True)
    card_number = Column(INTEGER, nullable=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    created_by = Column(String(255))
    updated_by = Column(String(255))
