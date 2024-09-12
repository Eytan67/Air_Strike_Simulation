import json

path = '../files/aircrafts.json'#----------------------------------


# def read_txt_file(path: str) -> str:
#     my_file = open(path, "r", newline='', encoding="utf-8")
#
#     data = my_file.read()
#
#     my_file.close()
#     data = json.loads(data)
#
#     return data
# aircrafts_dict = read_txt_file(path)
#---------------------------



def score(aircraft_dict, speed_evaluation_unit, fuel_capacity_evaluation_unit):

    score_speed = aircraft_dict['speed']/speed_evaluation_unit
    score_fuel_capacity = aircraft_dict['fuel_capacity']/fuel_capacity_evaluation_unit
    full_score = "{:.2f}".format(score_speed + score_fuel_capacity)

    aircraft_dict['score'] = full_score
    print(aircraft_dict)
    return full_score

def calculate_aircraft_priority(aircrafts_dict):
    aircrafts = aircrafts_dict['aircrafts']

    max_speed = max(aircrafts_dict['aircrafts'], key=lambda x: x['speed'])['speed']
    min_speed = min(aircrafts_dict['aircrafts'], key=lambda x: x['speed'])['speed']
    speed_evaluation_unit = (max_speed - min_speed)/len(aircrafts_dict['aircrafts'])

    max_fuel_capacity = max(aircrafts_dict['aircrafts'], key=lambda x: x['fuel_capacity'])['fuel_capacity']
    min_fuel_capacity = min(aircrafts_dict['aircrafts'], key=lambda x: x['fuel_capacity'])['fuel_capacity']
    fuel_capacity_evaluation_unit = (max_fuel_capacity - min_fuel_capacity) / len(aircrafts_dict['aircrafts'])

    scoreds = [score(aircraft, speed_evaluation_unit, fuel_capacity_evaluation_unit) for aircraft in aircrafts ]
    return max(scoreds)




# calculate_aircraft_priority(aircrafts_dict)