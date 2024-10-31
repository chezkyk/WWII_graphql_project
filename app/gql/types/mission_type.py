import graphene as g


class MissionType(g.ObjectType):
    mission_id = g.Int()
    mission_date = g.Date()
    airborne_aircraft = g.Float()
    attacking_aircraft = g.Float()
    bombing_aircraft = g.Float()
    aircraft_returned = g.Float()
    aircraft_failed = g.Float()
    aircraft_damaged = g.Float()
    aircraft_lost = g.Float()

