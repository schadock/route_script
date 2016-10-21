from city import City
from road import Road
from route_options import RouteOptions
from road_missing import RoadMissing

def main():
    krakow    = City('Krakow'   , 50.060, 19.959)
    poznan    = City('Poznan'   , 52.399, 16.900)
    stargard  = City('Stargard' , 53.340, 15.020)
    szczecin  = City('Szczecin' , 53.430, 14.529)
    warszawa  = City('Warszawa' , 52.259, 21.020)
    wroclaw   = City('Wroclaw'  , 51.110, 17.030)
    all_roads = [
        Road(krakow,   poznan,      100.0),
        Road(krakow,   szczecin,    100.0),
        Road(krakow,   wroclaw,     100.0),

        Road(poznan,   krakow,      100.0),
        Road(poznan,   szczecin,    100.0),
        Road(poznan,   wroclaw,     100.0),
        Road(poznan,   warszawa,    100.0),

        Road(poznan, stargard, 100.0),
        Road(stargard, poznan, 100.0),
        Road(stargard, szczecin, 100.0),
        Road(stargard, wroclaw, 100.0),
        Road(szczecin, stargard, 100.0),
        Road(wroclaw, stargard, 100.0),
        Road(warszawa, stargard, 100.0),

        Road(szczecin, poznan,      100.0),
        Road(szczecin, krakow,      100.0),
        Road(szczecin, wroclaw,     100.0),

        Road(warszawa, poznan,      100.0),
        Road(warszawa, wroclaw,     100.0),
        Road(warszawa, krakow,      100.0),
        Road(warszawa, szczecin,    100.0),

        Road(wroclaw, poznan,       100.0),
        Road(wroclaw, szczecin,     100.0)
    ]

    route_options = RouteOptions(all_roads)
    starting_city = warszawa
    cities_to_visit = [szczecin, stargard, poznan, wroclaw]
    print("Fastest route from " + starting_city.name + " for:")
    show_cities_to_visit(cities_to_visit)
    shortest_route = []
    try:
        shortest_route = route_options.shortest_route(starting_city, cities_to_visit)
    except RoadMissing:
        print("Route didn't exist.")
    show_route(shortest_route)
    print("--------------------------")
    # starting_city = warszawa
    # cities_to_visit = [szczecin, stargard, poznan, wroclaw]
    # print("Longest route from " + starting_city.name + " for:")
    # show_cities_to_visit(cities_to_visit)
    # longest_route = []
    # try:
    #     longest_route = route_options.longest_route(starting_city, cities_to_visit)
    # except RoadMissing:
    #     print("Route didn't exist.")
    # show_route(longest_route)

def show_cities_to_visit(cities_to_visit):
    for city in cities_to_visit:
        print(city.name, end=", ")
    print(" ")

def show_route(route):
    if route:
        print("Route: ")
        for road in route:
            print(road.from_city.name + " --> " + road.to_city.name)

if __name__ == '__main__':
    main()