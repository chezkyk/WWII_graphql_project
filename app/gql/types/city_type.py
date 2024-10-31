import graphene as g


class CityType(g.ObjectType):
    city_id = g.Int()
    city_name = g.String()
    country_id = g.Int()
    latitude = g.String()
    longitude = g.String()

    country = g.Field("app.gql.types.CountryType")
