from road import Road
from city import City
from road_missing import RoadMissing
import datetime

class RouteOptions:
    """
    Count shortest and longest route based on geographic coordinate.

    :param [Road] all_roads: All roads between cities.
    """
    def __init__(self, all_roads):
        self.all_roads = all_roads

    def shortest_route(self, starting_city, cities_to_visit):
        """
        Return shortest route based on localization and max speed on route.

        :param  City   starting_city  : City where we start ride.
        :param  list   cities_to_visit: List of visited cities.

        :rtype: [City]
        """
        current_city = starting_city
        shortest_route = []
        for city in cities_to_visit[:]:
            shortest_road = self._select_road_base_on(self._shorter_time, current_city, cities_to_visit)
            shortest_route.append(shortest_road)
            current_city = shortest_road.to_city
        return shortest_route

    def longest_route(self, starting_city, cities_to_visit):
        """
        Return longest route based on localization and max speed on route.

        :param  City   starting_city  : City where we start ride.
        :param  list   cities_to_visit: List of visited cities.

        :rtype: [City]
        """
        current_city = starting_city
        longest_route = []
        for city in cities_to_visit[:]:
            longest_road = self._select_road_base_on(self._longer_time, current_city, cities_to_visit)
            longest_route.append(longest_road)
            current_city = longest_road.to_city
        return longest_route

    def _select_road_base_on(self, compare_method, current_city, cities_to_visit):
        """
        Return proper road for request.

        :param  City     current_city   : Current city
        :param  [City]   cities_to_visit: List of cities to visit.
        :param  callback compare_method : Method to compare ride time.

        :rtype: Road
        """
        all_roads_on_route = self._roads_from(current_city, cities_to_visit)
        chosen_road = self._compare_ride_time(all_roads_on_route, compare_method)
        cities_to_visit.remove(chosen_road.to_city)
        return chosen_road

    def _roads_from(self, current_city, cities_to_visit):
        """
        Return list of roads between cities on route.

        :param  City    current_city   : Current city
        :param  [City]  cities_to_visit: List of cities to visit.

        :rtype: [Road]
        """
        all_roads_from_current_city = self._all_roads_from(current_city)
        return self._roads_on_route_from(cities_to_visit, all_roads_from_current_city)

    def _all_roads_from(self, current_city):
        """
        Search all existing roads from current city.

        :param  City    current_city: City for which looking for roads.

        :rtype: [Road]
        """
        roads_from_current_city = []
        for road in self.all_roads:
            if current_city == road.from_city:
                roads_from_current_city.append(road)
        return roads_from_current_city

    def _roads_on_route_from(self, cities_to_visit, roads_from_current_city):
        """
        Only roads to cities where we want to go.

        :param  [City]  cities_to_visit        : List of cities to visit.
        :param  [Road]  roads_from_current_city: Roads list from current city.

        :rtype: [Road]
        """
        roads_between_cities = []
        for road in roads_from_current_city:
            for city in cities_to_visit:
                if road.to_city == city:
                    roads_between_cities.append(road)
        if not roads_between_cities:
            raise RoadMissing()
        return roads_between_cities

    def _shorter_time(self, shorter_ride_time, current_ride_time):
        """
        Condition for compare time for shortest ride time.

        :param  datetime shorter_ride_time: Shortest time to compare.
        :param  datetime current_ride_time: Time to compare.

        :rtype: bool
        """
        return shorter_ride_time > current_ride_time

    def _longer_time(self, longer_ride_time, current_ride_time):
        """
        Condition for compare time for longest ride time.

        :param  datetime longer_ride_time : Longest time to compare.
        :param  datetime current_ride_time: Time to compare.

        :rtype: bool
        """
        return longer_ride_time < current_ride_time

    def _compare_ride_time(self, roads, method_for_compare_ride_time):
        """
        Find shortest road from roads list.

        :param  [Road]   roads                       : List roads from current city.
        :param  callback method_for_compare_ride_time: Method to compare ride time.

        :rtype: Road
        """
        for road in roads:
            current_ride_time = Road(road.from_city, road.to_city, road.maxspeed).calculate_ride_time()
            if roads[0] == road:
                result_ride_time = current_ride_time
                result_road = road
            elif method_for_compare_ride_time(result_ride_time, current_ride_time):
                result_ride_time = current_ride_time
                result_road = road
        return result_road