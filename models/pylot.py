class Pylot:
    def __init__(self, name:str, skill_level:int):
        self.name = name
        self.skill_level = skill_level

    def __str__(self):
        return f'name: {self.name}, skill_level: {self.skill_level}'