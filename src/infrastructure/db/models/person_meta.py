from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Text, TIMESTAMP, func
from db.models import db

class PersonMeta(db.Model):
    __tablename__ = 'person_meta'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    person_id = Column(UUID(as_uuid=True), nullable=False)
    key = Column(String(255), nullable=False)
    value = Column(Text, nullable=True)
    date_created = Column(TIMESTAMP, server_default=func.now())
    date_modified = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())