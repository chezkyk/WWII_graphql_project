import graphene as g


class CountryType(g.ObjectType):
    country_id = g.Int()
    country_name = g.String()

    cities = g.List("app.gql.types.CityType")
