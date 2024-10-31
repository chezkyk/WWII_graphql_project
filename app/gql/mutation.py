import graphene as g

from app.gql.mutations.mission_mutations import AddMissionMutation, DeleteMissionMutation, UpdateMissionMutation
from app.gql.mutations.target_mutations import AddTargetMutation


class Mutation(g.ObjectType):
    add_new_mission = AddMissionMutation.Field()
    add_new_target = AddTargetMutation.Field()
    update_mission = UpdateMissionMutation.Field()
    delete_mission = DeleteMissionMutation.Field()