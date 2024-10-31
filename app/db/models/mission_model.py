from sqlalchemy import Column, Integer, String, ForeignKey, Float,Date

from app.db.models import Base

class Mission(Base):
    __tablename__ = 'missions'
    mission_id    = Column(Integer, primary_key=True)
    mission_date  = Column(Date)
    airborne_aircraft  = Column(Float)
    attacking_aircraft  = Column(Float)
    bombing_aircraft  = Column(Float)
    aircraft_returned  = Column(Float)
    aircraft_failed  = Column(Float)
    aircraft_damaged  = Column(Float)
    aircraft_lost = Column(Float)

    def to_dict(self):
        return {
            "mission_id": self.mission_id,
            "mission_date": self.mission_date.isoformat() if self.mission_date else None,
            "airborne_aircraft": self.airborne_aircraft,
            "attacking_aircraft": self.attacking_aircraft,
            "bombing_aircraft": self.bombing_aircraft,
            "aircraft_returned": self.aircraft_returned,
            "aircraft_failed": self.aircraft_failed,
            "aircraft_damaged": self.aircraft_damaged,
            "aircraft_lost": self.aircraft_lost
        }