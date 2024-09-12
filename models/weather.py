class Weather():
    def __init__(self, weather:str, clouds:int, wind:str):
        self.weather = weather
        self.clouds = clouds
        self.wind = wind

    def __str__(self):
        return f'{self.weather} {self.clouds} {self.wind}'