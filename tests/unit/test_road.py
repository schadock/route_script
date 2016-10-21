import unittest
import datetime
from road import Road
from city import City

class RoadTest(unittest.TestCase):
    """
    Test class Road Test if it get correct ride time for road.
    """
    def setUp(self):
        self.szczecin = City('Szczecin', 53.430, 14.529)
        self.warszawa = City('Warszawa', 52.259, 21.020)

    def test_calculate_ride_time(self):
        """
        Check correct calculate ride time.
        """
        ride_time = Road(self.szczecin, self.warszawa, maxspeed=100).calculate_ride_time()
        expected_ride_time = datetime.timedelta(hours=7, minutes=19, seconds=23, microseconds=520000)
        self.assertEquals(ride_time, expected_ride_time)