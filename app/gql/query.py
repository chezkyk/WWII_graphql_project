import graphene as g

from app.db.database import session_maker
from app.db.models.mission_model import Mission
from app.gql.types.mission_type import MissionType


class Query(g.ObjectType):
    mission_by_id = g.Field(MissionType, id=g.Int())
    missions_by_date = g.List(MissionType ,start_date= g.Date(), end_date=g.Date())

    def resolve_mission_by_id(self,info, id):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_id == id).first()

    def resolve_missions_by_date(self, info,start_date, end_date):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()


