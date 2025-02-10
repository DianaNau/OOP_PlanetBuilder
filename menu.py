import time
import os
from planet import Planet
from human import Human
from buildings import Buildings
from exit_program import exit_program
 
class MainMenu:
    def __init__(self):
        self.planets = []  # Liste für erstellte Planeten
 
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
 
    def show_planets(self):
        """Zeigt alle gespeicherten Planeten an."""
        if not self.planets:
            print("Keine Planeten vorhanden.\n")
        else:
            print("Aktuelle Planeten:")
            for planet in self.planets:
                print(f"- {planet.name}")
            print()
 
    def create_planet(self):
        """Erstellt einen neuen Planeten."""
        name = input("Gib den Namen des neuen Planeten ein: ")
        new_planet = Planet(name)
        self.planets.append(new_planet)
        print(f"Der neue Planet {new_planet.name} wurde erstellt!")
        time.sleep(2)
 
    def add_human_to_planet(self):
        """Fügt einem ausgewählten Planeten einen Menschen hinzu."""
        if not self.planets:
            print("Es gibt keine Planeten, auf denen Menschen hinzugefügt werden können.")
            time.sleep(2)
            return
 
        self.show_planets()
        planet_name = input("Wähle einen Planeten aus, um einen Menschen hinzuzufügen: ")
        planet = next((p for p in self.planets if p.name == planet_name), None)
 
        if planet:
            name = input("Gib den Namen des Menschen ein: ")
            age = int(input("Gib das Alter des Menschen ein: "))
            job = input("Gib den Beruf des Menschen ein: ")
            new_human = Human(name=name, age=age, job=job)
            planet.add_human(new_human)
            time.sleep(2)
        else:
            print(f"Planet {planet_name} nicht gefunden. Bitte versuche es erneut.")
            time.sleep(2)
 
    def build_building_on_planet(self):
        """Ermöglicht das Bauen eines Gebäudes auf einem ausgewählten Planeten."""
        if not self.planets:
            print("Es gibt keine Planeten, auf denen Gebäude gebaut werden können.")
            time.sleep(2)
            return
 
        self.show_planets()
        planet_name = input("Wähle einen Planeten aus, auf dem du ein Gebäude bauen möchtest: ")
        planet = next((p for p in self.planets if p.name == planet_name), None)
 
        if planet:
            Buildings.show_available_buildings()
            building_name = input("Gib den Namen des Gebäudes ein, das du bauen möchtest: ")
            building = next((b for b in Buildings.BUILDING_LIST if b["name"] == building_name), None)
 
            if building:
                if planet.can_afford_building(building):
                    planet.build(building)
                    time.sleep(2)
                else:
                    print(f"Nicht genug Ressourcen, um {building_name} auf {planet.name} zu bauen.")
                    time.sleep(2)
            else:
                print(f"Gebäude {building_name} nicht gefunden. Bitte versuche es erneut.")
                time.sleep(2)
        else:
            print(f"Planet {planet_name} nicht gefunden. Bitte versuche es erneut.")
            time.sleep(2)
 
    def show_planet_details(self):
        """Zeigt Details eines ausgewählten Planeten."""
        if not self.planets:
            print("Es gibt keine Planeten, deren Details angezeigt werden können.")
            time.sleep(2)
            return
 
        self.show_planets()
        planet_name = input("Wähle einen Planeten aus, um Details anzuzeigen: ")
        planet = next((p for p in self.planets if p.name == planet_name), None)
 
        if planet:
            self.clear_console()
            print(f"Details für {planet.name}:\n")
            planet.show_population()  # Zeigt die Bevölkerung
            planet.show_resources()  # Zeigt die Ressourcen
            planet.show_buildings()  # Zeigt die Gebäude
            input("\nDrücke Enter, um zurückzukehren.")
        else:
            print(f"Planet {planet_name} nicht gefunden. Bitte versuche es erneut.")
            time.sleep(2)
 
    def run(self):
        """Startet das Hauptmenü."""
        while True:
            self.clear_console()
            self.show_planets()
            print("Hauptmenü:")
            print("1: Neuen Planeten erstellen")
            print("2: Menschen hinzufügen")
            print("3: Gebäude bauen")
            print("4: Details eines Planeten anzeigen")
            print("5: Programm beenden")
            choice = input("Wähle eine Option: ")
 
            if choice == "1":
                self.create_planet()
            elif choice == "2":
                self.add_human_to_planet()
            elif choice == "3":
                self.build_building_on_planet()
            elif choice == "4":
                self.show_planet_details()
            elif choice == "5":
                exit_program()
            else:
                print("Ungültige Eingabe. Bitte versuche es erneut.")
                time.sleep(2)
 
 
 
