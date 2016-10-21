from math import radians, cos, sin, asin, sqrt
import datetime

class Road:
    """
    Count ride time based on geographic coordinate.

    :param City  from_city: City class object
    :param City  to_city  : City class object
    :param float maxspeed : Max ride speed on road.
    """
    def __init__(self, from_city, to_city, maxspeed):
        self.from_city = from_city
        self.to_city = to_city
        self.maxspeed = maxspeed

    def calculate_ride_time(self):
        """
        Calculate ride time between cities in hours.

        :rtype: datetime
        """
        distance = self._distance(self.from_city, self.to_city)
        ride_time_not_converted = distance / self.maxspeed
        ride_time = self._datetime_from(ride_time_not_converted)
        return ride_time

    def _datetime_from(self, hours):
        """
        Convert float to datetime.

        :param   float    hours: Ride time in hours in float type.
        :rtype:  datetime
        """
        return datetime.timedelta(hours=hours)

    def _distance(self, from_city, to_city):
        """
        Calculate the great  _by_haversine circle distance between two points
        on the earth (specified in decimal degrees)

        :rtype: float
        """
        lon1, lat1, lon2, lat2 = map(radians,
                                     [from_city.longitude, from_city.latitude, to_city.longitude, to_city.latitude])

        delta_longitude = lon2 - lon1
        delta_latitude = lat2 - lat1
        distance = 2 * asin(
            sqrt(sin(delta_latitude / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_longitude / 2) ** 2)) * 6371
        return round(distance, 2)

