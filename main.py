import math

from Readers import csv_reader, txt_reader, json_reader
from Calculators import aircraft_priority
from models import aircraft
from models.aircraft import Aircraft
from models.pylot import Pylot
from models.target import Target
from weather_reqwest import get_location



aircraft_path = './files/aircrafts.json'
pylots_path = './files/pylots.json'
target_path = './files/target.json'

origin = get_location('Haifa')

# load and handle aircrafts data
aircraft_data = json_reader.read_json_file(aircraft_path)
Aircraft.full_score = aircraft_priority.calculate_aircraft_priority(aircraft_data)
aircrafts = [Aircraft(aircraft['type'], aircraft['speed'], aircraft['fuel_capacity'], aircraft['score']) for aircraft in aircraft_data['aircrafts']]
print(Aircraft.full_score)

# load and handle pylots data
pylots_data = json_reader.read_json_file(pylots_path)
pylots = [Pylot(pylot['name'], pylot['skill_level']) for pylot in pylots_data['pilots']]
print(pylots_data)

# load and handle targets data
targets_data = json_reader.read_json_file(target_path)
targets = []
for target in targets_data['targets']:
    location = get_location(target['City'], key)
    target = Target(target['City'], target['Priority'], location['lat'], location['lon'])
    targets.append(target)
print(targets)

#calaulate the potential missions














class Pilot:
  def __init__(self, name:str, skill:int):
    self.name = name
    self.skill = skill


weights = {
    "distance" : 0.15,
    "aircraft_type" : 0.20,
    "pilot_skill" : 0.20,
    "weather_conditions" : 0.20,
    "execution_time" : 0.10,
    "priority":0.15
}
