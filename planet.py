from buildings import Buildings

class Planet:
    def __init__(self, name):
        self.name = name
        self.population = []  # Liste für die Menschen auf dem Planeten
        self.max_population = 20  # Maximale Bevölkerungszahl
        self.buildings = []  # Liste der gebauten Gebäude
        self.resources = {"food": 1000, "stone": 5000, "wood": 5000, "gold": 1000}  # Beispielressourcen
        self.has_townhall = False  # Indikator, ob ein Rathaus gebaut wurde

    def add_human(self, human):
        if not self.has_townhall:
            print("Kein Rathaus vorhanden! Ein Rathaus muss zuerst gebaut werden.")
            if not self.build_townhall():
                print("Der Mensch konnte nicht hinzugefügt werden.")
                return

        if len(self.population) < self.max_population:
            if self.resources["food"] >= 100:  # Prüft, ob genug Nahrung für den neuen Menschen verfügbar ist
                self.population.append(human)
                self.resources["food"] -= 100  # Nahrung wird bei der Erstellung eines Menschen abgezogen
                print(f"{human.name} wurde zu {self.name} hinzugefügt.")
            else:
                print("Nicht genügend Nahrung, um einen neuen Menschen hinzuzufügen.")
        else:
            print(f"Maximale Bevölkerungszahl von {self.max_population} auf {self.name} erreicht. {human.name} konnte nicht hinzugefügt werden.")

    def can_afford_building(self, building):
        return (
            self.resources["food"] >= building["food_costs"]
            and self.resources["stone"] >= building["stone_costs"]
            and self.resources["wood"] >= building["wood_costs"]
            and self.resources["gold"] >= building["gold_costs"]
        )

    def build(self, building):
        if self.can_afford_building(building):
            self.resources["food"] -= building["food_costs"]
            self.resources["stone"] -= building["stone_costs"]
            self.resources["wood"] -= building["wood_costs"]
            self.resources["gold"] -= building["gold_costs"]
            self.buildings.append(building["name"])
            if building["name"].lower() == "rathaus":
                self.has_townhall = True
            print(f"{building['name']} wurde auf {self.name} gebaut.")
        else:
            print(f"Nicht genug Ressourcen, um {building['name']} auf {self.name} zu bauen.")

    def build_townhall(self):
        townhall = next((b for b in Buildings.BUILDING_LIST if b["name"] == "Rathaus"), None)
        if townhall:
            if self.can_afford_building(townhall):
                self.build(townhall)
                return True
        print("Nicht genügend Ressourcen, um ein Rathaus zu bauen.")
        return False

    def show_buildings(self):
        if not self.buildings:
            print(f"Es gibt noch keine Gebäude auf {self.name}.")
        else:
            print(f"Gebäude auf {self.name}:")
            for building in self.buildings:
                print(f"- {building}")
