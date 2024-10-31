import graphene as g

from app.gql.types import MissionType
from app.db.database import session_maker

from app.db.models.mission_model import Mission
from app.db.models.target_model import TargetModel
from app.db.models.city_model import City
from app.db.models.country_model import Country

class Query(g.ObjectType):
    mission_by_id = g.Field(MissionType, id=g.Int())
    missions_by_date = g.List(MissionType ,start_date= g.Date(), end_date=g.Date())
    mission_by_country = g.List(MissionType ,country=g.String())
    mission_by_target_industry = g.List(MissionType,target_industry=g.String())
    # results_of_attack_by_type_of_attack = g.List()

    def resolve_mission_by_id(self,info, id):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_id == id).first()

    def resolve_missions_by_date(self, info,start_date, end_date):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()

    def resolve_mission_by_country(self, info, country):
        with session_maker() as session:
            return (session.query(Mission)
                    .join(Mission.targets)
                    .join(TargetModel.city)
                    .join(City.country).filter(Country.country_name == country).all())

    def resolve_mission_by_target_industry(self, info, target_industry):
        with session_maker() as session:
            return (session.query(Mission)
                    .join(Mission.targets)
                    .filter(TargetModel.target_industry == target_industry).all())




