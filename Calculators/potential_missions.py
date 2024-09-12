from Calculators.distance import haversine_distance
from models.mission import Mission
from models.target import Target
from weather_reqwest import get_weather_data

def calculat_potential_missions(targets:list[Target], pylots, aircrafts, origin):
    for target in targets:
        distance = haversine_distance(target.lat, target.lon, origin['lat'], origin['lon'])
        weather = get_weather_data(target.city)
        for pylot in pylots:
            for aircraft in aircrafts:
                Mission(target, pylot, aircraft, distance, weather)