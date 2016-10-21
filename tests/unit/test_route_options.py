import unittest
from road import Road
from city import City
from road_missing import RoadMissing
from route_options import RouteOptions

class RouteOptionsTest(unittest.TestCase):
    """
    Test class Route Option if it get correct shortest and longest route.
    """
    def setUp(self):
        self.krakow =   City('Krakow',   50.060, 19.959)
        self.poznan =   City('Poznan',   52.399, 16.900)
        self.szczecin = City('Szczecin', 53.430, 14.529)
        self.warszawa = City('Warszawa', 52.259, 21.020)
        self.wroclaw =  City('Wroclaw',  51.110, 17.030)
        self.city_without_roads = City("No where", 0.0, 0.0)

        self.krakow_poznan      = Road(self.krakow,     self.poznan,    100)
        self.krakow_szczecin    = Road(self.krakow,     self.szczecin,  100)
        self.krakow_warszawa    = Road(self.krakow,     self.warszawa,  100)
        self.krakow_wroclaw     = Road(self.krakow,     self.wroclaw,   100)

        self.poznan_krakow      = Road(self.poznan,     self.krakow,    100)
        self.poznan_szczecin    = Road(self.poznan,     self.szczecin,  100)
        self.poznan_waszawa     = Road(self.poznan,     self.warszawa,  100)
        self.poznan_wroclaw     = Road(self.poznan,     self.wroclaw,   100)

        self.szczecin_krakow    = Road(self.szczecin,   self.krakow,    100)
        self.szczecin_poznan    = Road(self.szczecin,   self.poznan,    100)
        self.szczecin_warszawa  = Road(self.szczecin,   self.warszawa,  100)
        self.szczecin_wroclaw   = Road(self.szczecin,   self.wroclaw,   100)

        self.warszawa_krakow    = Road(self.warszawa,   self.krakow,    100)
        self.warszawa_poznan    = Road(self.warszawa,   self.poznan,    100)
        self.warszawa_szczecin  = Road(self.warszawa,   self.szczecin,  100)
        self.warszawa_wroclaw   = Road(self.warszawa,   self.wroclaw,   100)

        self.wroclaw_krakow     = Road(self.wroclaw,    self.krakow,    100)
        self.wroclaw_poznan     = Road(self.wroclaw,    self.poznan,    100)
        self.wroclaw_szczecin   = Road(self.wroclaw,    self.szczecin,  100)
        self.wroclaw_warszawa   = Road(self.wroclaw,    self.warszawa,  100)

        self.poznan_wroclaw_faster = Road(self.poznan,  self.wroclaw,   120)
        self.wroclaw_krakow_faster = Road(self.wroclaw, self.krakow,    150)

        self.all_roads = [
            self.krakow_poznan, self.krakow_szczecin, self.krakow_warszawa, self.krakow_wroclaw,
            self.poznan_krakow, self.poznan_szczecin, self.poznan_waszawa, self.poznan_wroclaw, self.poznan_wroclaw_faster,
            self.szczecin_krakow, self.szczecin_poznan, self.szczecin_warszawa, self.szczecin_wroclaw,
            self.warszawa_krakow, self.warszawa_poznan, self.warszawa_szczecin, self.warszawa_wroclaw,
            self.wroclaw_krakow, self.wroclaw_krakow_faster, self.wroclaw_poznan, self.wroclaw_szczecin, self.wroclaw_warszawa
            ]
        self.roads_with_max_speed_100 = [
            self.krakow_poznan, self.krakow_szczecin, self.krakow_warszawa, self.krakow_wroclaw,
            self.poznan_krakow, self.poznan_szczecin, self.poznan_waszawa, self.poznan_wroclaw,
            self.szczecin_krakow, self.szczecin_poznan, self.szczecin_warszawa, self.szczecin_wroclaw,
            self.warszawa_krakow, self.warszawa_poznan, self.warszawa_szczecin, self.warszawa_wroclaw,
            self.wroclaw_krakow, self.wroclaw_poznan, self.wroclaw_szczecin, self.wroclaw_warszawa
            ]
        self.missing_roads = [self.szczecin_poznan, self.szczecin_wroclaw, self.wroclaw_krakow]

        self.route_options_with_roads_with_max_speed_100 = RouteOptions(self.roads_with_max_speed_100)
        self.route_options_with_all_roads = RouteOptions(self.all_roads)
        self.route_options_with_missing_roads = RouteOptions(self.missing_roads)

    def test_shortest_route_for_roads_with_speed_limit(self):
        """
        Check correction of get shortest route for roads with max speed limit 100.
        """
        cities_to_visit = [self.wroclaw, self.krakow, self.poznan]
        shortest_route = self.route_options_with_roads_with_max_speed_100.shortest_route(self.szczecin, cities_to_visit)
        expected_shortest_route = [self.szczecin_poznan, self.poznan_wroclaw, self.wroclaw_krakow]
        self.assertEquals(shortest_route, expected_shortest_route)

    def test_shortest_route_for_all_roads(self):
        """
        Check correction of get shortest route for roads with different speed.
        """
        cities_to_visit = [self.wroclaw, self.krakow, self.poznan]
        shortest_route = self.route_options_with_all_roads.shortest_route(self.szczecin, cities_to_visit)
        expected_shortest_route = [self.szczecin_poznan, self.poznan_wroclaw_faster, self.wroclaw_krakow_faster]
        self.assertEquals(shortest_route, expected_shortest_route)

    def test_cant_find_shortest_route_for_city_without_road(self):
        """
        Check if shortest route give exception when on cities visit list is city without roads.
        """
        invalid_cities_to_visit = [self.wroclaw, self.warszawa, self.city_without_roads]
        with self.assertRaises(RoadMissing):
            self.route_options_with_roads_with_max_speed_100.shortest_route(self.szczecin, invalid_cities_to_visit)

    def test_cant_find_shortest_route_for_cities_without_road_between_them(self):
        """
        Check if shortest route give exception when road between cities didn't exist.
        """
        cities_to_visit = [self.wroclaw, self.krakow, self.poznan]
        with self.assertRaises(RoadMissing):
            self.route_options_with_missing_roads.shortest_route(self.szczecin, cities_to_visit)

    def test_longest_route_for_roads_with_speed_limit(self):
        """
        Check correction of get longest route for roads with max speed limit 100.
        """
        cities_to_visit = [self.wroclaw, self.krakow, self.poznan]
        longest_route = self.route_options_with_roads_with_max_speed_100.longest_route(self.szczecin, cities_to_visit)
        expected_longest_route = [self.szczecin_krakow, self.krakow_poznan, self.poznan_wroclaw]
        self.assertEquals(longest_route, expected_longest_route)

    def test_longest_route_for_all_roads(self):
        """
        Check correction of get longest route for roads with different speed.
        """
        cities_to_visit = [self.wroclaw, self.krakow, self.poznan]
        longest_route = self.route_options_with_all_roads.longest_route(self.szczecin, cities_to_visit)
        expected_longest_route = [self.szczecin_krakow, self.krakow_poznan, self.poznan_wroclaw]
        self.assertEquals(longest_route, expected_longest_route)

    def test_cant_find_longest_route_for_city_without_road(self):
        """
        Check if longest route give exception when on cities visit list is city without roads.
        """
        invalid_cities_to_visit = [self.wroclaw, self.warszawa, self.city_without_roads]
        with self.assertRaises(RoadMissing):
            self.route_options_with_roads_with_max_speed_100.longest_route(self.szczecin, invalid_cities_to_visit)

    def test_cant_find_longest_route_for_cities_without_road_between_them(self):
        """
        Check if longest route give exception when road between cities didn't exist.
        """
        cities_to_visit = [self.wroclaw, self.krakow, self.poznan]
        with self.assertRaises(RoadMissing):
            self.route_options_with_missing_roads.longest_route(self.szczecin, cities_to_visit)