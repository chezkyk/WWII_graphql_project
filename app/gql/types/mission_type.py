import graphene as g
from app.db.models.mission_model import Mission


class MissionType(g.ObjectType):
    mission_id = g.Int()
    mission_date = g.Date()
    airborne_aircraft = g.Int()
    attacking_aircraft = g.Int()
    bombing_aircraft = g.Int()
    aircraft_returned = g.Int()
    aircraft_failed = g.Int()
    aircraft_damaged = g.Int()
    aircraft_lost = g.Int()
