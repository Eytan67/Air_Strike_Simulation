from Calculators.calculat_fit_score import calculate_fit_score
from models.aircraft import Aircraft
from models.pylot import Pylot
from models.target import Target
from models.weather import Weather


class Mission:
    def __init__(self, target:Target, pylot:Pylot, aircraft:Aircraft, distance:int, weather_conditions:Weather):
        self.target_city = target.city
        self.priority = target.priority
        self.assigned_pylot = pylot.name
        self.assigned_aircraft = aircraft.tipe
        self.distance = distance
        self.weather_conditions = weather_conditions
        self.pylot_skill = pylot.skill_level
        self.aircraft_speed = aircraft.speed
        self.aircraft_capacity = aircraft.fuel_capacity
        self.mission_fit_score = calculate_fit_score(target.priority, aircraft, pylot.skill_level, weather_conditions)

    def __str__(self):
        return f'target_city: {self.target_city}, priority: {self.priority}, assigned_pylot{self.assigned_pylot}, '
