class City:
    """
    Class create cities with longitude and latitude.

    :param str   name     : City name
    :param float longitude: Longitude geographic coordinate.
    :param float latitude : Latitude  geographic coordinate.
    """
    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude