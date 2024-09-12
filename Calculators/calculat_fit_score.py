from models.aircraft import Aircraft
from models.weather import Weather

max_target_score = 5
max_aircraft_score = Aircraft.full_score
max_pylot_score = 10
max_weather_score = 100


def calculate_fit_score(target_priority, aircraft, pylot_skill_level, weather_conditions):
    target_part_score = 100 * (target_priority / max_target_score)
    aircraft_part_score = 100 * (aircraft.score / max_aircraft_score)
    pylot_part_score = 100 * (pylot_skill_level / max_pylot_score)
    weahter_part_score = 100 * (calculate_wether_score(weather_conditions) / max_weather_score)

    fit_score = target_part_score * weights['priority'] \
                + aircraft_part_score * weights['aircraft_type']\
                + pylot_part_score * weights['pilot_skill']\
                + weahter_part_score * weights['weather_conditions']
    return fit_score

def calculate_wether_score(weather_conditions:Weather):
    return weather_score(weather_conditions.weather) * weather_conditions.clouds%10 * weather_conditions.wind

weights = {
    "distance" : 0.15,
    "aircraft_type" : 0.20,
    "pilot_skill" : 0.20,
    "weather_conditions" : 0.20,
    "execution_time" : 0.10,
    "priority":0.15
}

def weather_score(weather):
    if weather["condition"] == "Clear":
        return 1.0
    elif weather["condition"] == "Clouds":
        return 0.7
    elif weather["condition"] == "Rain":
        return 0.4
    elif weather["condition"] == "Stormy":
        return 0.2
    else:
        return 0