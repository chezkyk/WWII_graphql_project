import graphene as g


class TargetTypeType(g.ObjectType):
    target_type_id = g.Int()
    target_type_name = g.String()
    targets = g.List("app.gql.types.TargetType")
