from sqlalchemy import Column, Integer, String, ForeignKey, Float,Date
from sqlalchemy.orm import relationship

from app.db.models import Base

class TargetModel(Base):
    __tablename__ = 'targets'
    target_id    = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry  = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('target_types.target_type_id'))
    target_priority = Column(Integer)

    city = relationship('City')
    # target_type = relationship('TargetTypeModel')
    mission = relationship("Mission", back_populates="targets")