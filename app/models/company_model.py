from datetime import datetime

from sqlalchemy import FLOAT, INTEGER, Column, DateTime, String

from app.common.database import DBBaseCustom


class CompanyModel(DBBaseCustom):
    __tablename__ = "companies"
    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(255), nullable=False)
    unit_cost = Column(FLOAT, nullable=False)
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
