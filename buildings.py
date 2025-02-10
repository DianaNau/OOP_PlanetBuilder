class Buildings:
    BUILDING_LIST = [
        {"name": "Rathaus", "food_costs": 50, "stone_costs": 1200, "wood_costs": 1200, "gold_costs": 80},
        {"name": "Jägerhütte", "food_costs": 10, "stone_costs": 10, "wood_costs": 200, "gold_costs": 30},
        {"name": "Bauernhof", "food_costs": 20, "stone_costs": 400, "wood_costs": 1200, "gold_costs": 50},
        {"name": "Holzfällerhütte", "food_costs": 10, "stone_costs": 100, "wood_costs": 300, "gold_costs": 25},
        {"name": "Steinbruch", "food_costs": 15, "stone_costs": 100, "wood_costs": 1200, "gold_costs": 25},
        {"name": "Goldmine", "food_costs": 40, "stone_costs": 1500, "wood_costs": 1500, "gold_costs": 30},
    ]

    @staticmethod
    def show_available_buildings():
        """Zeigt eine Liste der verfügbaren Gebäude und deren Kosten."""
        print("Verfügbare Gebäude:")
        for building in Buildings.BUILDING_LIST:
            print(
                f"{building['name']} - Nahrung: {building['food_costs']}, Stein: {building['stone_costs']}, "
                f"Holz: {building['wood_costs']}, Gold: {building['gold_costs']}"
            )
        print()
