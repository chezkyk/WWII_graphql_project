import graphene as g


class TargetType(g.ObjectType):
    target_id = g.Int()
    mission_id = g.Int()
    target_industry = g.String()
    city_id = g.Int()
    target_type_id = g.Int()
    target_priority = g.Int()
