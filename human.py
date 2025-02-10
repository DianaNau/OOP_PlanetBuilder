import random 

class Human:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

        
def create_humans(planet, number):
    """
    Fügt eine Anzahl von Menschen zur Bevölkerung eines Planeten hinzu.
   
    Args:
        planet (Planet): Der Planet, auf dem Menschen erschaffen werden sollen.
        number (int): Die Anzahl der Menschen, die erschaffen werden sollen.
    """
    planet.population += number
    print(f"{number} Menschen wurden auf dem Planeten {planet.name} erschaffen!")

