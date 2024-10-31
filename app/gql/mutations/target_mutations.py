import graphene as g
from sqlalchemy import Integer

from app.db.database import session_maker
from app.db.models.mission_model import Mission
from app.db.models.target_model import TargetModel
from app.db.models.target_type_model import TargetTypeModel
from app.gql.types import MissionType, TargetType


class AddTargetMutation(g.Mutation):
    class Arguments:
        target_id = g.Int(required=True)
        mission_id = g.Int(required=True)
        target_industry = g.String()
        city_id = g.Int(required=True)
        target_type_id = g.Int(required=True)
        target_priority = g.String()

    success = g.Boolean()
    target = g.Field(TargetType)

    @staticmethod
    def mutate(root, info, target_id, mission_id, target_industry, city_id, target_type_id, target_priority):
        with session_maker() as session:
            inserted_target = TargetModel(target_id=target_id, mission_id=mission_id, target_industry=target_industry,
                                          city_id=city_id, target_type_id=target_type_id, target_priority=target_priority)
            session.add(inserted_target)
            session.commit()
            session.refresh(inserted_target)
            return AddTargetMutation(target=inserted_target,success=True)

