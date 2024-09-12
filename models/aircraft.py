class Aircraft:
    full_score = 0
    def __init__(self, tipe:str, speed:int, fuel_capacity:int, score:float):
        self.tipe = tipe
        self.speed = speed
        self.fuel_capacity = fuel_capacity
        self.score = score

    def __str__(self):
        return f"tipe: {self.tipe}, speed: {self.speed}, fuel_capacity: {self.fuel_capacity}, score: {self.score}"