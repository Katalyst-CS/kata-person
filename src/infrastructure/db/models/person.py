from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date, TIMESTAMP, func
from src.infrastructure.db.models import db

class Person(db.Model):
    __tablename__ = 'person'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    given_name = Column(String(100), nullable=False)
    family_name = Column(String(200), nullable=False)
    additional_name = Column(String(200), nullable=True)
    birth_date = Column(Date, nullable=True)
    gender = Column(String(1), nullable=True)
    date_created = Column(TIMESTAMP, server_default=func.now())
    date_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())