import graphene as g

from app.db.database import session_maker
from app.db.models.mission_model import Mission
from app.db.models.target_model import TargetModel
from app.gql.types import MissionType


class AddMissionMutation(g.Mutation):
    class Arguments:
        mission_id = g.Int(required=True)
        mission_date = g.Date()
        airborne_aircraft = g.Float()
        attacking_aircraft = g.Float()
        bombing_aircraft = g.Float()
        aircraft_returned = g.Float()
        aircraft_failed = g.Float()
        aircraft_damaged = g.Float()
        aircraft_lost = g.Float()

    success = g.Boolean()
    mission = g.Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, mission_date,
               airborne_aircraft,attacking_aircraft,bombing_aircraft,
               aircraft_returned, aircraft_failed, aircraft_damaged,aircraft_lost):
        with session_maker() as session:
            inserted_mission = Mission(mission_id=mission_id,mission_date=mission_date,airborne_aircraft=airborne_aircraft,
                                       attacking_aircraft=attacking_aircraft,
                                       bombing_aircraft=bombing_aircraft,
                                       aircraft_returned=aircraft_returned,
                                       aircraft_failed=aircraft_failed,
                                       aircraft_damaged=aircraft_damaged,
                                       aircraft_lost=aircraft_lost)
            session.add(inserted_mission)
            session.commit()
            session.refresh(inserted_mission)
            return AddMissionMutation(mission=inserted_mission,success=True)

class UpdateMissionMutation(g.Mutation):
    class Arguments:
        mission_id = g.Int(required=True)
        mission_date = g.Date()
        airborne_aircraft = g.Float()
        attacking_aircraft = g.Float()
        bombing_aircraft = g.Float()
        aircraft_returned = g.Float()
        aircraft_failed = g.Float()
        aircraft_damaged = g.Float()
        aircraft_lost = g.Float()

    success = g.Boolean()
    mission = g.Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, mission_date=None,
               airborne_aircraft=None, attacking_aircraft=None, bombing_aircraft=None,
               aircraft_returned=None, aircraft_failed=None, aircraft_damaged=None, aircraft_lost=None):
        with session_maker() as session:
            mission = session.query(Mission).get(mission_id)
            if mission is None:
                raise Exception('Mission not found')

            if mission_date is not None:
                mission.mission_date = mission_date
            if airborne_aircraft is not None:
                mission.airborne_aircraft = airborne_aircraft
            if attacking_aircraft is not None:
                mission.attacking_aircraft = attacking_aircraft
            if bombing_aircraft is not None:
                mission.bombing_aircraft = bombing_aircraft
            if aircraft_returned is not None:
                mission.aircraft_returned = aircraft_returned
            if aircraft_failed is not None:
                mission.aircraft_failed = aircraft_failed
            if aircraft_damaged is not None:
                mission.aircraft_damaged = aircraft_damaged
            if aircraft_lost is not None:
                mission.aircraft_lost = aircraft_lost

            session.commit()
            return UpdateMissionMutation(mission=mission, success=True)


class DeleteMissionMutation(g.Mutation):
    class Arguments:
        mission_id = g.Int(required=True)

    success = g.Boolean()

    @staticmethod
    def mutate(root, info, mission_id):
        with session_maker() as session:
            mission = session.query(Mission).filter_by(mission_id=mission_id).first()
            if not mission:
                raise Exception("Mission not found")

            session.query(TargetModel).filter_by(mission_id=mission_id).delete()
            session.query(Mission).filter_by(mission_id=mission_id).delete()

            session.delete(mission)
            session.commit()
            return DeleteMissionMutation(success=True)
