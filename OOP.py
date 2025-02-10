# Klassen
import random
 
class Planet:
   
    def __init__(self, name):
        self.name = name # Instanzattribut
        self.population = random.randint(10000, 50000)
        self.food = random.randint(1000, 2000)
    
 
       
   
 
    def __str__(self):
        return f"Planet :{self.name} Bevölkerung: {self.population} Nahrung: {self.food}"
 
   
 
 
planet1 = Planet("Erde")
planet2 = Planet("Mars")
print(planet1)
print(planet2)
 
