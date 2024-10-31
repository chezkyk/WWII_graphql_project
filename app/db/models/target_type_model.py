from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.models import Base

class TargetTypeModel(Base):
    __tablename__ = 'target_types'
    target_type_id   = Column(Integer, primary_key=True)
    target_type_name  = Column(String)

