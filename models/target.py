class Target():
    targets_distanc = 0
    def __init__(self, city:str, priority:int, lat:float, lon:float):
        self.city = city
        self.priority = priority
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'city: {self.city}, priority: {self.priority}, lat: {self.lat}, lon: {self.lon}'
